## 10. Common Pitfalls & Anti-Patterns

### Pitfall 1: `sleep()` in E2E Tests

```typescript
// ❌ BAD: Arbitrary sleep — flaky on slow machines, wastes time on fast ones
await page.waitForTimeout(3000);
await sleep(2000);

// ✅ GOOD: Wait for the actual condition your test needs
await page.waitForResponse(r => r.url().includes('/api/orders') && r.status() === 201);
await expect(page.getByTestId('order-confirmation')).toBeVisible({ timeout: 10_000 });
await page.waitForSelector('[data-testid="success-banner"]:not([aria-hidden])');
// RULE: If you catch yourself typing "sleep", ask "what am I actually waiting for?"
```

### Pitfall 2: Shared Mutable State Between Tests

```typescript
// ❌ BAD: Tests share a user — one test's mutation bleeds into others
let sharedUser: User;
beforeAll(async () => {
  sharedUser = await createUser({ email: 'shared@test.com', credits: 100 });
});

test('deducts credits on purchase', async () => {
  await api.purchase(sharedUser.id, product);
  const user = await api.getUser(sharedUser.id);
  expect(user.credits).toBe(90);  // FLAKY: another test may have modified credits
});

// ✅ GOOD: Each test creates and owns its isolated data
test('deducts credits on purchase', async () => {
  const user = await createUser({ email: `test-${Date.now()}@example.com`, credits: 100 });
  await api.purchase(user.id, product);
  const updated = await api.getUser(user.id);
  expect(updated.credits).toBe(90);
  // Cleanup in afterEach or use factory with auto-teardown
});
```

### Pitfall 3: 100% Coverage as the Goal

```typescript
// ❌ BAD: Test that "covers" a line but asserts nothing meaningful
it('calls calculateTotal', () => {
  const result = calculateTotal([]);
  expect(result).toBeDefined();  // Always true — even if result is NaN or undefined
});

// Also bad: excluding code to hit the metric
// jest.config.js: coveragePathIgnorePatterns: ['./src/legacy/', './src/utils/']

// ✅ GOOD: Meaningful assertions that would fail if the logic broke
it('returns 0 for empty cart', () => {
  expect(calculateTotal([])).toBe(0);
});
it('sums item prices including tax', () => {
  expect(calculateTotal([{ price: 100, qty: 2 }], { taxRate: 0.1 })).toBe(220);
});
// BONUS: Use mutation testing to verify your tests actually catch bugs
// npx stryker run → mutation score > 70% is more valuable than 100% line coverage
```

### Pitfall 4: Skipping Non-Functional Testing

```yaml
# ❌ BAD: CI pipeline with no performance gate — "we'll load test later"
jobs:
  unit-tests: ...
  e2e-tests: ...
  deploy: needs: [e2e-tests]   # Ships with no performance or security validation

# ✅ GOOD: Non-functional tests are required CI stages
jobs:
  unit-tests: ...
  e2e-tests: ...
  performance-gate:
    needs: [e2e-tests]
    steps:
      - name: k6 smoke test
        uses: grafana/k6-action@v0.3.1
        with: { filename: tests/load/smoke.js }
        env: { BASE_URL: ${{ secrets.STAGING_URL }} }
  security-scan:
    needs: [e2e-tests]
    steps:
      - run: docker run --rm -t owasp/zap2docker-stable zap-baseline.py -t $STAGING_URL
  deploy:
    needs: [performance-gate, security-scan]  # Cannot deploy without both passing
```

### Pitfall 5: Giant Test Files with No Structure

```typescript
// ❌ BAD: 500-line test file with flat structure and no helpers
test('user can login', async () => { /* 50 lines of setup inline */ });
test('user can register', async () => { /* duplicates setup from above */ });
test('admin can delete user', async () => { /* more inline setup duplication */ });

// ✅ GOOD: Organized with describe blocks, shared fixtures, Page Object Model
describe('Authentication', () => {
  let authHelper: AuthHelper;

  beforeEach(async () => {
    authHelper = new AuthHelper(page);
  });

  describe('Login', () => {
    it('redirects to dashboard on success', async () => { /* focused, readable */ });
    it('shows error for invalid credentials', async () => { /* one assertion */ });
  });

  describe('Registration', () => {
    it('sends verification email after signup', async () => { /* focused */ });
  });
});
```
