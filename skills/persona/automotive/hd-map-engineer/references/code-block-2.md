# python Example

```
import numpy as np
from shapely.geometry import LineString

def compute_chamfer_distance(pred_polylines: list, gt_polylines: list) -> float:
    """
    Compute average Chamfer Distance between predicted and GT polylines.
    pred_polylines, gt_polylines: lists of (N, 2) numpy arrays (BEV coords)
    """
    if not pred_polylines or not gt_polylines:
        return float('inf')

    total_cd = 0.0
    count = 0
    for gt_poly in gt_polylines:
        gt_pts = gt_poly  # (N, 2)
        min_dists = []
        for pred_poly in pred_polylines:
            # Directed distance: GT -> nearest pred point
            pred_pts = pred_poly
            dists = np.min(
                np.linalg.norm(gt_pts[:, None, :] - pred_pts[None, :, :], axis=-1),
                axis=1)
            min_dists.append(np.mean(dists))
        total_cd += min(min_dists)
        count += 1
    return total_cd

# Decision thresholds for use case compatibility
USE_CASE_REQUIREMENTS = {
    'highway_lane_keep':     {'min_mIoU': 0.65, 'max_CD_m': 0.30},
    'urban_lane_keep':       {'min_mIoU': 0.60, 'max_CD_m': 0.40},
    'intersection_manage':   {'min_mIoU': 0.70, 'max_CD_m': 0.25},  # stricter
    'parking':               {'min_mIoU': 0.50, 'max_CD_m': 0.60},
}

def assess_use_case_compatibility(eval_results: dict, use_case: str) -> str:
    reqs = USE_CASE_REQUIREMENTS[use_case]
    if (eval_results['mIoU'] >= reqs['min_mIoU'] and
            eval_results['mean_CD_m'] <= reqs['max_CD_m']):
        return 'COMPATIBLE'
    return 'INSUFFICIENT — use offline HD map'
```
