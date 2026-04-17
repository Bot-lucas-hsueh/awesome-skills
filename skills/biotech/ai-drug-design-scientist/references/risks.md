## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|--------------------|------------|
| False positive ADMET predictions from in silico tools | HIGH | Compounds advanced without real liabilities flagged, wasting synthesis/testing resources | Always confirm with orthogonal wet-lab assays (kinetic solubility, microsomal stability, Caco-2) before major investment |
| Structure prediction errors in AlphaFold models (low pLDDT regions) | HIGH | Incorrect binding pocket geometry leads to wrong pharmacophore hypotheses and useless docking poses | Use only high-confidence regions (pLDDT > 70); confirm with experimental structure when progressing beyond hit stage |
| PAINS/reactive compound false negatives | HIGH | Compounds with promiscuous mechanisms selected as hits, corrupting SAR campaigns | Screen every compound against PAINS, Brenk, and NIH alert filters; validate with counter-assays (thermal shift, NMR) |
| Dataset bias in QSAR models | MEDIUM | Models trained on biased chemical series extrapolate poorly, misleading SAR interpretation | Define applicability domain; report RMSE and uncertainty on held-out external test set |
| Regulatory non-compliance in candidate selection | CRITICAL | IND rejection or clinical hold due to unresolved genotoxicity, hERG risk, or metabolic liabilities | Consult FDA/ICH guidelines (M7, S7B) early; flag genotoxic alerts and hERG predictions at lead stage |
| Intellectual property conflicts in generated structures | MEDIUM | AI-generated molecules may reproduce patented structures, creating freedom-to-operate issues | Run generated structures against patent databases (SureChEMBL, Derwent) before synthesis |
| Overconfidence in virtual screening rankings | HIGH | Docking scores are highly approximate; top-ranked virtual hits have low experimental confirmation rates (5-20%) | Treat docking results as hypothesis generators; require experimental validation before any resource commitment |

---
