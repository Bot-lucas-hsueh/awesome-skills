# Standards & Reference

## 7.1 Data Management Standards

- [DataCite Metadata Schema 4.4](https://schema.datacite.org/meta/kernel-4.4/) — Required metadata for DOI registration
- [Dublin Core Metadata Initiative](https://dublincore.org/specifications/dublin-core/) — Cross-disciplinary metadata terms
- [FAIR Data Principles](https://www.go-fair.org/fair-principles/) — Findable, Accessible, Interoperable, Reusable
- [DMPTool](https://dmptool.org/) — Data Management Plan creation aligned with funder requirements
- [NIH Data Management and Sharing Policy](https://sharing.nih.gov/) — Mandates data sharing for NIH-funded research
- [ORCID](https://orcid.org/) — Persistent identifier for researchers

## 7.2 Repository & Archiving Standards

| Platform | Type | Standards | URL |
|----------|------|----------|-----|
| **Zenodo** | General-purpose | DataCite, Dublin Core | https://zenodo.org |
| **Figshare** | General-purpose | DataCite | https://figshare.com |
| **Dryad** | General-purpose | DataCite | https://datadryad.org |
| **ICPSR** | Social science | DDI | https://icpsr.umich.edu |
| **NCAR** | Earth sciences | ISO 19115, CF conventions | https://ncar.ucar.edu |

## 7.3 Data Licensing Standards

| License | Use Case | Attribution | Commercial |
|---------|----------|------------|-----------|
| **CC0** | Public domain, open data | Not required | Yes |
| **CC-BY 4.0** | Recommended for research | Required | Yes |
| **CC-BY-NC 4.0** | Non-commercial research | Required | No |
| **ODC-ODbL** | Database rights | Required | Conditional |

## 7.4 FAIR Principles Implementation

| Principle | Actions |
|----------|--------|
| **Findable** | DOI assigned; rich metadata; searchable in registries |
| **Accessible** | Open protocol; long-term availability; metadata accessible |
| **Interoperable** | Standard vocabularies; provenance documented; standard formats |
| **Reusable** | Clear license; detailed documentation; machine-readable terms |

## 7.5 File Format Recommendations

| Data Type | Preferred | Acceptable | Avoid |
|----------|----------|-----------|-------|
| Tabular | CSV, TSV | Excel, JSON | .xls, proprietary |
| Text | Plain text, Markdown | PDF/A | .doc |
| Images | PNG, TIFF | JPEG | BMP |
| Code | Python, R, Julia | MATLAB | Closed formats |
| Geospatial | GeoJSON, NetCDF | Shapefile | Proprietary |

## 7.6 Data Management Plan Elements

| Funder | Required | Sharing Timeline | Notes |
|---------|---------|----------------|-------|
| NIH | Yes (2023+) | By publication | Plan required at application |
| NSF | Yes (per program) | Encouraged | No specific timeline |
| DOE | Yes | Publication + 3 years | Required |
| ERC (EU) | Yes | End of project | Open by default |
| Wellcome | Yes | By publication | Expected |
