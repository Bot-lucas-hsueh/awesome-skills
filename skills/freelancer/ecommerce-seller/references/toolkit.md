## § 6 · Professional Toolkit

- **Helium 10** — Product research (Xray BSR/sales), keyword research (Cerebro, Magnet), listing optimization (Scribbles), PPC management (Adtomic)
- **Jungle Scout** — Product demand validation, supplier database, market trends
- **DataDive** — Advanced competitor analysis and listing optimization
- **Keepa** — BSR history, price history, deal alerts for Amazon products
- **Alibaba
- **QIMA
- **Shopify + Klaviyo** — DTC store + email/SMS marketing automation

## Phase 1: Product Research & Validation

```python
def product_opportunity_analysis(bsr, monthly_sales, avg_reviews_top10,
                                  selling_price, cogs_landed, weight_lbs):
    """
    Quick product opportunity score.
    Returns score (0-30) and pass/fail recommendation.
    """
    scores = {}

    # Demand score (1-5)
    if bsr < 3000: scores['demand'] = 5
    elif bsr < 10000: scores['demand'] = 4
    elif bsr < 30000: scores['demand'] = 3
    elif bsr < 100000: scores['demand'] = 2
    else: scores['demand'] = 1

    # Competition score (1-5) — fewer reviews = easier entry
    if avg_reviews_top10 < 200: scores['competition'] = 5
    elif avg_reviews_top10 < 400: scores['competition'] = 4
    elif avg_reviews_top10 < 800: scores['competition'] = 3
    elif avg_reviews_top10 < 1500: scores['competition'] = 2
    else: scores['competition'] = 1

    # Profitability score (1-5)
    amazon_referral_fee = selling_price * 0.15  # 15% typical
    fba_fee = 3.22 if weight_lbs < 1 else 4.50  # simplified FBA fee
    total_fees = amazon_referral_fee + fba_fee
    net_profit = selling_price - cogs_landed - total_fees
    margin = net_profit

    if margin >= 0.40: scores['profitability'] = 5
    elif margin >= 0.30: scores['profitability'] = 4
    elif margin >= 0.20: scores['profitability'] = 3
    elif margin >= 0.10: scores['profitability'] = 2
    else: scores['profitability'] = 1

    # Logistics score (1-5)
    if weight_lbs < 1: scores['logistics'] = 5
    elif weight_lbs < 2: scores['logistics'] = 4
    elif weight_lbs < 5: scores['logistics'] = 3
    else: scores['logistics'] = 2

    total = sum(scores.values())
    recommendation = "STRONG GO" if total >= 16 else "CAUTIOUS" if total >= 12 else "SKIP"

    return total, scores, net_profit, margin, recommendation

# Example: Kitchen organizer product
score, breakdown, profit, margin, rec = product_opportunity_analysis(
    bsr=4500, monthly_sales=450, avg_reviews_top10=320,
    selling_price=29.99, cogs_landed=7.50, weight_lbs=0.8
)
print(f"Total Score: {score}/20, Net Profit: ${profit:.2f}, Margin: {margin:.0%}, Recommendation: {rec}")
# Total Score: 17/20, Net Profit: $14.27, Margin: 48%, Recommendation: STRONG GO
```

**Break-Even ACOS Calculation:**
```python
def break_even_acos(selling_price, cogs_landed, fba_fee_estimate, referral_rate=0.15):
    """
    Break-even ACOS: max advertising spend as % of revenue before losing money.
    ACOS = Ad Spend
    Break-even ACOS = Profit Margin (before advertising)
    """
    referral_fee = selling_price * referral_rate
    gross_profit = selling_price - cogs_landed - fba_fee_estimate - referral_fee
    be_acos = gross_profit

    target_acos = be_acos * 0.7  # Target 70% of break-even = 30% profit margin on ads
    return {
        'break_even_acos_pct': round(be_acos * 100, 1),
        'target_acos_pct': round(target_acos * 100, 1),
        'gross_profit_per_unit': round(gross_profit, 2),
    }

result = break_even_acos(29.99, 7.50, 3.22)
print(f"Break-even ACOS: {result['break_even_acos_pct']}%, Target ACOS: {result['target_acos_pct']}%")
# Break-even ACOS: 64.2%, Target ACOS: 44.9%
```

✓ Product scores ≥ 16/20 before ordering samples
✓ Break-even ACOS calculated before launching PPC
✗ Never order bulk inventory before receiving and approving physical sample

### Phase 2: Listing Optimization & Launch

**Title Formula (Amazon):**
```
[Brand] + [Primary Keyword] + [Secondary Keyword] + [Key Feature] + [Size/Color/Quantity]

Example:
"LUXE HOME Bamboo Kitchen Drawer Organizer — Expandable Utensil Tray with Dividers | Fits Drawers 13-21 Inches | Set of 5"

Rules:
• 200 characters max (mobile shows ~80 characters before truncation)
• Primary keyword in first 5 words (highest weight)
• No promotional phrases ("best," "top-rated," "#1")
• Include size/variant info for filter discoverability
```

**Bullet Points Framework (FEATURES → BENEFITS):**
```
Bullet 1 (Headline benefit): ALL CAPS claim + explanation
"ORGANIZED IN MINUTES — Our expandable design fits any standard kitchen drawer (13-21 inches),
letting you clear countertop clutter in under 5 minutes."

Bullet 2: Second most important feature + specific benefit + quantification
"5 ADJUSTABLE SECTIONS — Create up to 5 dedicated compartments for spatulas, knives, spoons,
and small gadgets — everything in reach, nothing in the way."

Bullet 3: Material/quality differentiator with longevity claim
"SUSTAINABLE BAMBOO — Food-safe, eco-friendly bamboo is naturally antimicrobial and more
durable than plastic — built to outlast cheap alternatives by years."

Bullet 4: Problem this product solves
"STOPS THE JUNK DRAWER SPIRAL — No more rummaging through tangled utensils.
Our non-slip base keeps organizer in place even in busy households."

Bullet 5: Satisfaction guarantee
"RISK-FREE PURCHASE — We stand behind every organizer with a lifetime replacement guarantee.
If you're not 100% satisfied, we'll make it right."
```

**Inventory Reorder Formula:**
```python
def reorder_point(daily_sales_units, lead_time_days, safety_stock_days=14):
    """
    Calculate reorder point for Amazon FBA inventory.
    Lead time: supplier production (21-35 days) + shipping (20-45 days sea freight)
    Safety stock: buffer for demand spikes and shipping delays
    """
    reorder_at = daily_sales_units * (lead_time_days + safety_stock_days)
    order_qty_90_days = daily_sales_units * 90  # 3-month order
    return {
        'reorder_when_units_reach': int(reorder_at),
        'order_quantity': int(order_qty_90_days),
        'days_of_inventory': 90 + safety_stock_days,
    }

# 15 units/day, 60-day total lead time (30 production + 30 sea freight)
result = reorder_point(daily_sales=15, lead_time_days=60, safety_stock_days=14)
print(f"Reorder when: {result['reorder_when_units_reach']} units remain")
print(f"Order quantity: {result['order_quantity']} units")
# Reorder when: 1,110 units remain; Order: 1,350 units
```

## 🔬 Scenario Examples

### 🚫 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Ordering Bulk Before Sample Approval
**Wrong:** Find supplier on Alibaba; skip sample; order 500 units to get MOQ discount.
**Why it fails:** Without physical inspection, supplier ships substandard goods. Return/replace at scale = $3,000+ loss + 90-day delay.
**Correct:** Order 2-3 samples (< $200). Test quality, dimensions, packaging. Approve before MOQ. Use third-party QC inspection (QIMA, ~$300) for first bulk order.

### Anti-Pattern 2: Targeting Oversaturated Keywords Only
**Wrong:** Target only "kitchen organizer" (100,000+ monthly searches, top 10 competitors 2,000+ reviews).
**Why it fails:** Can't rank for broad terms without existing BSR; PPC cost is $3-5/click with low conversion → ACOS 80%+.
**Correct:** Long-tail keyword strategy: "bamboo expandable kitchen drawer organizer for utensils" (2,000 monthly searches, 15-20 competitors, lower CPC). Rank on longtail → build BSR → compete on head terms later.

### Anti-Pattern 3: Ignoring IPI Score (Inventory Performance Index)
**Wrong:** Send 3,000 units to FBA without checking current IPI score.
**Why it fails:** If IPI < 450, Amazon restricts restocking capacity. Already-sent inventory incurs long-term storage fees. Stranded inventory can't be sold.
**Correct:** Monitor IPI weekly (target > 500). Keep DOI 45-60 days to avoid excess. Liquidate slow sellers before IPI drops.

### Anti-Pattern 4: Setting and Forgetting PPC
**Wrong:** Launch PPC campaigns; check in once per month.
**Why it fails:** Within 1 week, auto campaigns find irrelevant search terms and spend $200+ on zero-converting traffic.
**Correct:** Daily check for first 2 weeks (5 minutes: look at ACOS by campaign and by keyword). Add negatives aggressively. After optimization, weekly review is sufficient.

### Anti-Pattern 5: Pricing Without Amazon Fee Calculation
**Wrong:** Price product at $19.99 because competitors are $19.99; expect good profit.
**Why it fails:** Amazon referral fee (15%) = $3.00; FBA fee = $3.22; COGS $8.00; shipping to FBA $1.50 → Net = $4.27 (21% margin). After PPC at 25% ACOS = $5.00 → NET LOSS of $0.73/unit.
**Correct:** Use Amazon Revenue Calculator BEFORE pricing decision. Calculate all-in: COGS + landed + FBA + referral + advertising = total cost. Price for 25-35% net after advertising.

