# Real-World Examples

## 10.1 Cart Abandonment Reduction Campaign

**Scenario:** An apparel DTC brand has a 73% cart abandonment rate. Post-purchase surveys indicate 40% of abandoners cite "shipping costs too high" and 25% cite "need to create an account."

**Approach:**
1. **Diagnosis:** Implement full-funnel analytics with GA4 enhanced ecommerce. Tag all checkout steps to identify exact drop-off points. Cross-reference with heatmaps to see where users hesitate.

2. **Intervention - Shipping Transparency:** Add a zip-code shipping estimator on the cart page. Offer free shipping at $75 threshold (was $100). Test "free shipping over $75" vs. "flat $5.99 shipping" using a 50/50 A/B test.

3. **Intervention - Account Friction:** Enable guest checkout with post-purchase account creation offer ("Save your info for 10% off next order"). Compare guest vs. account checkout funnel conversion rates.

4. **Intervention - Exit Intent:** Deploy exit-intent popup offering 10% off first order in exchange for email. Integrate with Klaviyo for abandoned cart email sequence (1hr, 24hr, 72hr with discount code).

5. **Results:** After 4 weeks, cart abandonment dropped to 64%. Guest checkout increased checkout completions by 12%. Email capture added 3,200 subscribers. Net revenue impact: +18% from recovered carts.

## 10.2 Checkout Redesign for Mobile Commerce

**Scenario:** A beauty brand's mobile conversion rate is 1.2%, half the desktop rate of 2.4%. Mobile accounts for 65% of traffic but only 45% of revenue. The checkout flow has 9 form fields and requires account creation.

**Approach:**
1. **Audit:** Use Microsoft Clarity to watch session recordings of mobile users. Find common friction points: small tap targets, long dropdowns for country/state, unexpected account creation wall.

2. **Redesign Principles:**
   - Reduce to 5 fields: email, shipping address, payment, shipping method
   - Use address autocomplete (addressy) for all address fields
   - Replace dropdowns with smart defaults (pre-fill country, guess state from IP)
   - Surface express pay: Apple Pay, Google Pay, Shop Pay buttons above fold

3. **A/B Test Design:**
   - Control: existing 9-field checkout
   - Variant: 5-field with express pay
   - Primary metric: checkout completion rate
   - Secondary: time-to-purchase, mobile-specific NPS
   - Minimum sample: 1,000 completed orders per variant before statistical significance

4. **Results:** Variant achieved 3.1% mobile conversion (vs 1.2% control), a 158% improvement. Average time to purchase reduced from 4 min to 90 seconds. Apple Pay accounted for 34% of mobile orders.

## 10.3 A/B Test Design for Pricing Strategy

**Scenario:** A home goods e-commerce site wants to test whether offering a "pay in 4" installment option (Klarna/Afterpay) increases conversion rate without reducing AOV.

**Approach:**
1. **Hypothesis:** Displaying a "4 interest-free payments of $X" option below the price will increase conversion for price-sensitive segments (new visitors, mobile users) while preserving AOV for credit-worthy segments.

2. **Test Design:**
   - Traffic split: 50/50
   - Control: standard price display ("$199.99")
   - Variant: standard price + installment messaging ("4 interest-free payments of $49.99")
   - Segment analysis: New vs. returning visitors, mobile vs. desktop, order value tiers

3. **Measurement:**
   - Primary: conversion rate per session
   - Secondary: AOV, add-to-cart rate, product page engagement
   - Guardrail: Check that installment users don't have higher return rates

4. **Results:** Installment messaging increased conversion by 22% overall. AOV remained stable (+1%, not statistically significant). New visitor conversion lifted 31%. No increase in return rates. Recommended permanent rollout.

## 10.4 Product Information Migration to PIM

**Scenario:** A multi-brand retailer selling across Amazon, their own website, and 3 wholesale channels has inconsistent product data. Product titles vary across channels, descriptions are outdated, and images are wrong or missing. SEO rankings are declining.

**Approach:**
1. **Assessment:** Audit current state across all channels. Count total SKUs. Identify data gaps: missing attributes (material, dimensions), inconsistent naming conventions, image count per SKU.

2. **PIM Selection:** Evaluate Akeneo (open source), inRiver, and Salsify. Chose Akeneo for open API and lower TCO. Key requirements: bulk import from supplier spreadsheets, auto-translation for marketplace listings, workflow approval for wholesale pricing.

3. **Data Migration:**
   - Consolidate all product data into central PIM
   - Standardize attributes: title format ("Brand - Product Name - Variant - Size/Color"), description template
   - Map GS1 GPC category codes for Amazon requirement
   - Enrich: add alt text to all images, technical specifications, dimension tables

4. **Distribution:** Push corrected data to all channels via connectors. Set up automated publishing workflow: PIM update → quality check → publish to channels.

5. **Results:** Product listing error rate dropped from 23% to 2%. Amazon listing quality score improved from 67 to 94. Organic search traffic increased 15% within 60 days from improved product schema markup.

## 10.5 Personalization Rollout for Returning Visitors

**Scenario:** A sporting goods e-commerce site wants to increase repeat purchase rate by showing personalized product recommendations based on browsing and purchase history. They have 2M registered users.

**Approach:**
1. **Data Infrastructure:** Implement Salesforce Commerce Cloud Einstein Recommendations. Feed behavioral events: page views, add-to-cart, purchases, wishlist adds. Set up 30-day data lookback window for relevance.

2. **Recommendation Strategy by Page:**
   - Homepage: "Based on your recent browsing" (behavioral)
   - Cart page: "Complete the look" / "Frequently bought together" (collaborative filtering)
   - Post-purchase: "Your next essentials" with replenishment reminders for consumables
   - PLP: "Sort by popularity among similar shoppers"

3. **Testing:** First run a holdout test — 20% of users see random/non-personalized recommendations as control. Measure add-to-cart lift, conversion lift, and AOV lift over 4 weeks.

4. **Transparency & Trust:** Label all recommendations with "Because you viewed X" or "Popular with customers like you." Add a "See all recommendations" toggle to show non-personalized fallback.

5. **Results:** Personalized recommendations drove 18% higher add-to-cart rate vs. control. Conversion rate for returning visitors increased 9%. Revenue per session on personalized pages was 23% higher. User opt-out rate for personalization was under 1%.
