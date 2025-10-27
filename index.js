import express from 'express';
const app = express();
app.get('/health', (req, res) => res.json({ ok: true }));
app.listen(4000, '0.0.0.0', () => console.log('Backend running on port 4000'));