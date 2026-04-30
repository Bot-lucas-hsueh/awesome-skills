# DoorDash Engineering Anti-Patterns

## #DD1: Single-Side Optimization

❌ **Wrong**: Optimizing only for consumer experience (fastest possible delivery) without considering dasher earnings or merchant capacity.

✅ **Right**: Every optimization considers impact on all three sides of the marketplace.

## #DD2: Ignoring Submarket Differences

❌ **Wrong**: Applying the same dispatch parameters across all cities without considering local patterns.

✅ **Right**: Submarket-specific models with localized parameters for each city/neighborhood.

## #DD3: Over-Batching

❌ **Wrong**: Stacking too many orders to maximize efficiency, degrading quality for all customers.

✅ **Right**: Quality score gates prevent batching when it would hurt customer experience.

## #DD4: Underestimating Prep Time

❌ **Wrong**: Dispatching dasher immediately when order placed, causing long wait at restaurant.

✅ **Right**: ML-predicted prep time determines optimal order firing time.

## #DD5: Static ETAs

❌ **Wrong**: Fixed delivery time estimates that don't adapt to real-time conditions.

✅ **Right**: Dynamic ETAs that update based on traffic, restaurant status, and dasher location.

## #DD6: Ignoring Peak Patterns

❌ **Wrong**: Same supply positioning on Super Bowl Sunday as a regular Sunday.

✅ **Right**: Event-aware demand forecasting with pre-positioned supply.

## #DD7: Zero-Sum Promotions

❌ **Wrong**: Aggressive discounts that attract unprofitable customers without growing the marketplace.

✅ **Right**: Targeted promotions that expand the marketplace and improve unit economics.

## #DD8: Feature Launch Without A/B Test

❌ **Wrong**: Rolling out changes to 100% of users without measuring impact.

✅ **Right**: Every change A/B tested with statistical significance before full rollout.

## #DD9: Siloed Metrics

❌ **Wrong**: Optimizing team metrics in isolation (e.g., dispatch efficiency) without considering cross-functional impact.

✅ **Right**: North Star metrics that reflect overall marketplace health.

## #DD10: Forget Dasher Experience

❌ **Wrong**: Designing systems that optimize for dispatch efficiency but create frustrating dasher experience.

✅ **Right**: Dasher-centric design with earnings transparency and route quality.
