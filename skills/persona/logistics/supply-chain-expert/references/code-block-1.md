# python Example

```
import numpy as np

def safety_stock(service_level_pct, avg_daily_demand, std_daily_demand,
                  avg_lead_time_days, std_lead_time_days):
    """
    Safety stock with combined demand and lead time variability.
    SS = Z × σ_LTD where σ_LTD = √(L×σ_d² + d²×σ_L²)
    """
    Z_map = {90: 1.282, 95: 1.645, 97: 1.881, 98: 2.054, 99: 2.326, 99.9: 3.090}
    Z = Z_map.get(service_level_pct, 1.645)
    sigma_LTD = np.sqrt(avg_lead_time_days * std_daily_demand**2 +
                         avg_daily_demand**2 * std_lead_time_days**2)
    SS = Z * sigma_LTD
    return {'safety_stock_units': round(SS), 'Z_factor': Z, 'sigma_LTD': round(sigma_LTD, 1)}

def economic_order_quantity(annual_demand, ordering_cost, unit_cost, carrying_rate=0.25):
    """
    Economic Order Quantity (EOQ) — Wilson formula.
    H = unit_cost × carrying_rate (annual holding cost per unit)
    Carrying rate typically 20-30% (storage, capital, obsolescence, handling).
    """
    H = unit_cost * carrying_rate
    EOQ = np.sqrt(2 * annual_demand * ordering_cost
    reorder_frequency = annual_demand
    return {
        'EOQ_units': round(EOQ),
        'orders_per_year': round(reorder_frequency, 1),
        'annual_holding_cost': round(EOQ
        'annual_ordering_cost': round(reorder_frequency * ordering_cost),
    }

def reorder_point(avg_daily_demand, avg_lead_time_days, safety_stock_units):
    """ROP = (avg_daily_demand × avg_lead_time) + safety_stock"""
    return round(avg_daily_demand * avg_lead_time_days + safety_stock_units)

def inventory_metrics(COGS, avg_inventory_value):
    """
    Key inventory performance metrics.
    Industry benchmarks: Retail 4-8x, Auto 10-15x, FMCG 8-12x turns.
    """
    turns = COGS
    DIO = 365
    return {'inventory_turns': round(turns, 1), 'DIO_days': round(DIO)}

# Example: 95% service level, 100 units/day demand, σ=20, 14d lead time, σ_LT=3d
ss_result = safety_stock(95, 100, 20, 14, 3)
# SS = 1.645 × √(14×400 + 10000×9) = 1.645 × √(5600+90000) = 1.645 × 309 = 508 units
rop = reorder_point(100, 14, ss_result['safety_stock_units'])
print(f"Safety Stock: {ss_result['safety_stock_units']} units | ROP: {rop} units")
```
