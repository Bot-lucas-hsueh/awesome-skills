# typescript Example

```
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
