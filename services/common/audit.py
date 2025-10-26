import json, time, hashlib, os
LOG_DIR = os.environ.get("LOG_DIR", "logs")
LOG_FILE = os.path.join(LOG_DIR, "audit_chain.jsonl")
os.makedirs(LOG_DIR, exist_ok=True)

def _hash(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def append_audit(event_type: str, payload: dict):
    ts = int(time.time())
    prev_hash = None
    # read last hash
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "rb") as f:
            try:
                *_, last = f.read().splitlines()
                prev = json.loads(last.decode("utf-8"))
                prev_hash = prev.get("record_hash")
            except ValueError:
                prev_hash = None
    record = {
        "ts": ts,
        "event": event_type,
        "payload": payload,
        "prev_hash": prev_hash,
    }
    record_str = json.dumps(record, sort_keys=True)
    record_hash = _hash(record_str)
    record["record_hash"] = record_hash
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return record_hash
