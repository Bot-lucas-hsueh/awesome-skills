# Troubleshooting Guide

## 8.1 Cart Abandonment

### High Cart Abandonment Rate (>70%)

**Symptoms:** Cart abandonment rate exceeds industry average of 65-70%.

**Diagnosis:**
1. Check mobile checkout flow completion rate vs. desktop
2. Review payment method availability by region
3. Audit unexpected costs (shipping, taxes) added late in checkout
4. Test guest vs. account checkout friction

**Solutions:**
- Enable guest checkout and offer express payment (Shop Pay, Apple Pay, Google Pay)
- Display shipping costs early via zip-code estimator before cart page
- Implement persistent cart recovery emails with 1hr/24hr/72hr cadence
- Reduce form fields: limit checkout to 5-8 essential fields max
- Add trust signals (security badges, return policy) near payment section

### Session-to-Cart Rate Low

**Symptoms:** Few visitors add items to cart despite high product page views.

**Diagnosis:**
1. Verify add-to-cart button visibility and responsiveness (not hidden by modals)
2. Check product page loading speed — images and CTA must render within 3s
3. Review product imagery and description quality
4. Confirm inventory is available and displayed correctly

**Solutions:**
- A/B test CTA button color, size, and copy ("Add to Bag" vs "Buy Now")
- Enable sticky add-to-cart on mobile product pages
- Ensure product images load via CDN with WebP/AVIF formats

## 8.2 Checkout Optimization

### Checkout Drop-off at Payment Step

**Symptoms:** Users reach payment step but do not complete purchase.

**Diagnosis:**
1. Test all payment methods in staging environment for errors
2. Check if card declined messaging is clear and offers alternatives
3. Review 3D Secure / SCA friction for European transactions
4. Verify SSL certificate validity and trust seal visibility

**Solutions:**
- Offer at least 3 payment methods: credit card, PayPal, and buy-now-pay-later (Klarna/Afterpay)
- Implement address autocomplete (Google Places / addressy) to reduce form friction
- Add inline validation so users see errors before submission
- Enable express checkout options (Shop Pay, Amazon Pay) to bypass guest checkout

### High Declined Transaction Rate

**Symptoms:** Payment gateway reports >15% decline rate.

**Diagnosis:**
1. Check fraud rules — too aggressive AVS or CVV thresholds
2. Verify payment gateway status and webhook delivery
3. Review address verification mismatch rate
4. Test with test cards from each major network (Visa, MC, Amex)

**Solutions:**
- Tune fraud rules: accept transactions with AVS match on zip only
- Enable retry logic with exponential backoff for transient failures
- Implement card updating via network tokens (Visa Token Service) to reduce declines from expired cards

## 8.3 Personalization & Search

### Search Converts Lower Than Browse

**Symptoms:** Site search users have lower conversion rate than navigation users.

**Diagnosis:**
1. Review zero-results page — does it offer alternatives?
2. Check search algorithm relevance scoring
3. Verify faceted navigation filters work correctly
4. Audit synonyms dictionary coverage

**Solutions:**
- Implement "no results" redirects to popular categories or related products
- Add type-ahead / autocomplete with popular queries
- Use behavioral signals (click-through, add-to-cart) to re-rank results
- Enable voice search and misspell tolerance

### Personalization Feels Creepy or Irrelevant

**Symptoms:** Users disable personalization or complain recommendations are off-target.

**Diagnosis:**
1. Check recommendation algorithm freshness — is it using outdated purchase data?
2. Verify recency weighting in collaborative filtering
3. Review why-new-user recommendations

**Solutions:**
- Add "Why recommended" labels to show algorithmic reasoning
- Limit behavioral data window to 30-90 days for relevance
- Offer opt-out of personalization with "Popular" fallback
- Never show products for life events (pregnancy, illness) without explicit signals

## 8.4 Platform-Specific Issues

### Shopify: Checkout Extension Not Loading

**Symptoms:** Custom checkout UI elements fail to render on Shopify Checkout.

**Diagnosis:**
1. Confirm extension uses Checkout UI extensions API (not legacy Shopify Scripts)
2. Check extension scope includes `checkout` and `payment-dispatch`
3. Verify extension is published and not in draft state

**Solutions:**
- Migrate from Shopify Scripts to Checkout UI Extensions for Shopify Functions
- Test in checkout editor with all payment methods enabled
- Follow Shopify's [checkout extension best practices](https://shopify.dev/docs/api/checkout-extensions)

### Magento: Product Images Not Loading

**Symptoms:** Product images show placeholder or 404 on PDP.

**Diagnosis:**
1. Check media directory permissions (var/ and pub/media/)
2. Verify catalog_product_entity_media_gallery database table
3. Confirm ImageMagick or GD extension is installed and configured

**Solutions:**
- Run `bin/magento catalog:images:resize` to regenerate cached images
- Set correct file permissions: 664 for files, 775 for directories
- Check .htaccess in media folder is not blocking direct access
- Verify CDN (Fastly/Cloudflare) cache purge was triggered on product save

## 8.5 Mobile Commerce

### Mobile Page Speed Score Below 70

**Symptoms:** Core Web Vitals failing, low mobile conversion.

**Diagnosis:**
1. Run Lighthouse on mobile with throttling
2. Check Largest Contentful Paint (LCP) > 2.5s, Cumulative Layout Shift (CLS) > 0.1
3. Audit third-party scripts: analytics, chat widgets, tag managers
4. Verify image optimization: sizing, lazy loading, format

**Solutions:**
- Implement critical CSS inlining for above-the-fold content
- Defer non-critical JavaScript; use async/defer attributes
- Use next-gen image formats (WebP, AVIF) with srcset fallbacks
- Preconnect to critical origins (fonts, CDN)
- Audit and delay/shadow-tag third-party scripts

### Mobile Add-to-Cart Not Responding

**Symptoms:** Tap on add-to-cart does nothing on iOS Safari.

**Diagnosis:**
1. Check for double-tap zoom interference on buttons
2. Verify touch events are not blocked by overlays
3. Test with Safari Web Inspector on connected iOS device

**Solutions:**
- Add `touch-action: manipulation` CSS to prevent 300ms tap delay
- Ensure buttons have minimum 44x44pt touch target
- Remove hover-dependent interactions from mobile flow
- Disable pinch-zoom only on the add-to-cart area, not the whole page
