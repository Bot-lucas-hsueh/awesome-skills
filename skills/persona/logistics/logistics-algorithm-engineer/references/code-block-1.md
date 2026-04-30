# python Example

```
# Data validation template
import numpy as np
import pandas as pd

def validate_vrp_input(customers_df, distance_matrix, vehicle_capacity):
    """
    Validate VRP input data before solving.
    Returns list of validation errors.
    """
    errors = []

    # Check coordinates
    if customers_df[['lat', 'lon']].isna().any().any():
        errors.append("NULL coordinates detected — fix before solving")

    # Check demands
    if (customers_df['demand'] < 0).any():
        errors.append(f"Negative demands: {(customers_df['demand'] < 0).sum()} records")

    oversized = customers_df[customers_df['demand'] > vehicle_capacity]
    if len(oversized) > 0:
        errors.append(f"Demand exceeds vehicle capacity: {len(oversized)} customers — needs split delivery")

    # Check time windows
    if 'time_window_open' in customers_df.columns:
        invalid_tw = customers_df[customers_df['time_window_open'] > customers_df['time_window_close']]
        if len(invalid_tw) > 0:
            errors.append(f"Infeasible time windows (open > close): {len(invalid_tw)} customers")

    # Check distance matrix
    n = len(distance_matrix)
    diag_violations = np.diag(distance_matrix).sum()
    if diag_violations > 0:
        errors.append("Non-zero diagonal in distance matrix")

    # Triangle inequality sample check (sample 1000 triplets)
    violations = 0
    sample_size = min(1000, n * (n-1) * (n-2) // 6)
    indices = np.random.choice(n, size=(sample_size, 3), replace=True)
    for a, b, c in indices:
        if a != b and b != c and a != c:
            if distance_matrix[a][c] > distance_matrix[a][b] + distance_matrix[b][c] + 1e-6:
                violations += 1
    if violations > 0:
        errors.append(f"Triangle inequality violations: {violations}

    return errors
```
