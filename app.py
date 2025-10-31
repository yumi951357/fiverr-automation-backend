@app.post("/neural/generator")
async def generate(req: TaskRequest, request: Request):
    ok = await verify_api_key(request)
    if not ok:
        return {"output": "⚠️ Unauthorized access — using fallback generator."}
    if not req.prompt:
        raise HTTPException(status_code=422, detail="Missing prompt in request")
    
    print(f"✅ Received prompt from frontend: {req.prompt}")
    
    # 智能解析用户请求
    prompt_lower = req.prompt.lower()
    
    if "expand" in prompt_lower and "section" in prompt_lower:
        # 用户要求扩展具体章节
        if "overview" in prompt_lower or "section 1" in prompt_lower:
            text = """**1. Overview - Expanded Content**

**Company Mission:**
To revolutionize e-commerce through AI-powered personalization and automation.

**Core Value Proposition:**
- Real-time customer behavior analysis
- Automated inventory optimization  
- Personalized marketing campaigns
- 24/7 AI customer support

**Target Market:** 
E-commerce businesses with $1M+ annual revenue seeking to scale operations through AI automation.

**Unique Selling Points:**
✓ Predictive analytics for demand forecasting
✓ Integration with major e-commerce platforms
✓ ROI-focused pricing model"""
        elif "market analysis" in prompt_lower or "section 2" in prompt_lower:
            text = """**2. Market Analysis - Expanded Content**

**Market Size & Growth:**
- Global e-commerce automation market: $18.3B (2024)
- Expected CAGR: 14.2% through 2030
- Target addressable market: $2.1B

**Competitive Landscape:**
- **Direct Competitors:** Shopify AI, BigCommerce Automation
- **Indirect Competitors:** Custom development agencies
- **Market Gap:** Lack of integrated, affordable AI solutions for mid-market e-commerce

**Customer Segmentation:**
1. **SMB E-commerce** ($1M-10M revenue) - 45% of market
2. **Enterprise Retail** ($10M+ revenue) - 35% of market  
3. **Agency Partners** (White-label) - 20% of market

**Trend Analysis:**
- Rising demand for personalized shopping experiences
- Increasing adoption of AI in inventory management
- Growing need for omnichannel automation"""
        else:
            text = f"AI Business Plan Draft for: {req.prompt}\n\n1. Overview\n2. Market Analysis\n3. Strategy\n4. Revenue Model\n5. Timeline"
    else:
        # 默认返回大纲
        text = f"AI Business Plan Draft for: {req.prompt}\n\n1. Overview\n2. Market Analysis\n3. Strategy\n4. Revenue Model\n5. Timeline"
    
    return {"output": text}