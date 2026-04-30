## 9. Real-World Scenarios

### Scenario 1: Building Test Coverage from Near Zero

**Context:** A team has < 10% test coverage on a 2-year-old codebase. The team wants to reach 80% without stopping feature work.

**QA Engineer Approach:**

> **Incremental Coverage Strategy — "Ratchet and Don't Slip"**
>
> **Phase 1: Stop the bleeding (Week 1)**
> - Add coverage threshold to CI: start at current baseline (e.g., 8%), fail if it drops
> - Every new PR must include tests for new code — enforce with coverage diff check
>
> ```yaml
> # .github/workflows/coverage-gate.yml
> - name: Coverage check (new code must be 80%+ covered)
>   run: |
>     npx jest --coverage --coverageThreshold='{"global":{"lines":8}}'
>     # Also check coverage of changed files using diff-cover
>     git diff origin/main --name-only | grep '\.ts$' > changed_files.txt
>     npx diff-cover coverage/lcov.info --compare-branch=origin/main --fail-under=80
> ```
>
> **Phase 2: Cover the critical paths (Weeks 2-6)**
> - Identify top 10 most business-critical modules (payments, auth, data processing)
> - Write tests for these first — 20% of the code often drives 80% of the risk
> - Use mutation testing to check if existing tests are meaningful
>
> ```bash
> # Stryker mutation testing — finds tests that pass even with bugs
> npx stryker run
> # Look for low mutation score modules — those tests aren't catching real bugs
> ```
>
> **Phase 3: Raise the bar incrementally (Months 2-6)**
> - Each sprint, raise the global threshold by 2-5%
> - Track coverage trend in Codecov — celebrate improvements in team retros
> - Refactor legacy code into testable units (dependency injection, pure functions)
>
> **Anti-patterns to avoid:**
> - Writing tests just to hit coverage numbers (testing getters/setters, trivial code)
> - Excluding large chunks of code from coverage reports
> - Prioritizing coverage % over test quality and meaningful assertions

### Scenario 2: Eliminating Flaky E2E Tests

**Context:** The E2E test suite has 30% flakiness rate. Engineers disable failing tests rather than fix them. CI is no longer trusted.

**QA Engineer Approach:**

> **Flaky Test Elimination — 3-Step Rescue Plan**
>
> **Step 1: Quarantine immediately — don't let flaky tests block CI**
> ```typescript
> // Mark known flaky tests explicitly — visible, not swept under the rug
> test.skip('FLAKY: checkout flow times out on payment step — JIRA QA-234', async ({ page }) => {
>   // ... test code preserved for fixing
> });
>
> // Playwright built-in retry for intermittent tests
> test('payment flow', { retries: 3 }, async ({ page }) => {
>   // If this passes on retry, it's flaky — investigate
> });
> ```
>
> **Step 2: Root cause analysis — 5 most common flakiness causes**
> ```typescript
> // CAUSE 1: Timing issues — never use arbitrary sleeps
> // BAD
> await page.waitForTimeout(3000);
>
> // GOOD — wait for the actual condition
> await page.waitForResponse(resp => resp.url().includes('/api/orders') && resp.status() === 201);
> await expect(page.getByTestId('order-confirmation')).toBeVisible();
>
> // CAUSE 2: Test data collision — tests sharing state
> // BAD — global test user modified by multiple tests
> // GOOD — each test creates its own isolated data
> test('updates user profile', async ({ page, request }) => {
>   const user = await request.post('/api/test/users', {
>     data: { email: `test-${Date.now()}@example.com` }
>   });
>   // Use this user and clean up in afterEach
> });
>
> // CAUSE 3: Network instability — add explicit waits
> await page.route('**/api/**', route => route.continue());
>
> // CAUSE 4: Animations interfering with click targets — disable in tests
> // playwright.config.ts
> use: {
>   launchOptions: { args: ['--disable-animations'] },
> }
> ```
>
> **Step 3: Measure and prevent regression**
> - Track flakiness rate per test weekly
> - Any test with > 5% flakiness rate gets a fix-or-delete decision within 2 weeks
> - Add test health dashboard to team's engineering metrics

### Scenario 3: Performance Testing a New Feature Before Release

**Context:** A new search feature is launching. The team has never done performance testing. The product expects 10x traffic growth.

**QA Engineer Approach:**

> **Performance Testing Checklist for Search Feature**
>
> **Step 1: Define performance requirements (before writing tests)**
> ```
> SLOs for Search API:
> - p50 response time < 100ms
> - p95 response time < 500ms
> - p99 response time < 2000ms
> - Error rate < 0.1%
> - Throughput: 1000 RPS sustained, 3000 RPS peak
> ```
>
> **Step 2: Smoke test → Load test → Stress test → Soak test**
> ```javascript
> // k6/search-smoke.js — Quick validation (5 VUs, 1 minute)
> export const options = { vus: 5, duration: '1m',
>   thresholds: { http_req_duration: ['p(99)<2000'] }
> };
>
> // k6/search-load.js — Normal expected load (ramp to 1000 RPS)
> export const options = {
>   stages: [
>     { duration: '5m', target: 500 },
>     { duration: '10m', target: 1000 },
>     { duration: '5m', target: 0 },
>   ],
>   thresholds: {
>     http_req_duration: ['p(95)<500', 'p(99)<2000'],
>     http_req_failed: ['rate<0.001'],
>   }
> };
>
> // k6/search-stress.js — Find the breaking point
> export const options = {
>   stages: [
>     { duration: '2m', target: 1000 },
>     { duration: '2m', target: 2000 },
>     { duration: '2m', target: 3000 },
>     { duration: '2m', target: 4000 },  // Expect failures here
>     { duration: '2m', target: 0 },
>   ],
>   thresholds: { http_req_failed: ['rate<0.1'] }  // Relaxed threshold for stress test
> };
> ```
>
> **Step 3: Correlate with infrastructure metrics**
> - Monitor DB query times during load test (slow queries identified under load)
> - Watch for connection pool exhaustion (psycopg2.OperationalError
> - Check cache hit rates (if cache is cold, performance will be misleading)
> - Use distributed tracing (Jaeger/Zipkin) to find bottlenecks in the hot path

### Scenario 4: Anti-Pattern — Testing Implementation Instead of Behavior

**Context:** A developer writes unit tests that mock and assert on internal method calls. Every refactor breaks 30 tests even though the feature still works correctly.

**The Anti-Pattern:**

```typescript
// ❌ ANTI-PATTERN: Testing implementation details
// These tests break on every refactoring, even if behavior is correct

describe('PricingService', () => {
  it('calls applyTierMultiplier with correct rate', () => {
    const spy = jest.spyOn(pricingService, 'applyTierMultiplier');
    pricingService.calculateDiscount(100, 'premium');
    // This test cares HOW it works, not WHAT it returns
    expect(spy).toHaveBeenCalledWith(0.9);
  });

  it('calls discountRepository.save', async () => {
    const saveSpy = jest.spyOn(discountRepo, 'save');
    await pricingService.applyDiscount(order);
    expect(saveSpy).toHaveBeenCalled();  // Tests the call, not the outcome
  });
});
```

**The QA Engineer Fix:**

```typescript
// ✅ CORRECT: Test observable behavior — survives any internal refactoring

describe('PricingService', () => {
  it.each([
    ['basic',      100, 100],   // No discount
    ['premium',    100, 90],    // 10% off
    ['enterprise', 100, 75],    // 25% off
  ] as const)('applies %s tier discount to price', (tier, price, expected) => {
    // Tests the OUTPUT — doesn't care about internal implementation
    expect(calculateDiscount(price, tier)).toBe(expected);
  });

  it('persists the discounted price to the order record', async () => {
    const order = await createTestOrder({ subtotal: 100 });
    await pricingService.applyDiscount(order, 'enterprise');

    // Verify the STATE CHANGE — not which method was called
    const updated = await orderRepo.findById(order.id);
    expect(updated.total).toBe(75);
    expect(updated.discountApplied).toBe(true);
  });
});

// WHY THIS MATTERS:
// - You can rename applyTierMultiplier() or replace it entirely → tests still pass
// - You can split discountRepository.save() into two calls → tests still pass
// - Tests that survived a refactor are tests that were actually testing behavior
```
