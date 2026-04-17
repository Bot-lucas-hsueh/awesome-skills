# 8. Annotation
vep -i analysis_ready.vcf.gz -o annotated.vcf.gz --cache --assembly GRCh38 \
  --plugin CADD,LoFtool --custom gnomad.vcf.gz,gnomADg,vcf,exact,0,AF,AF_afr,AF_eas
```

### Variant Classification (ACMG Guidelines)

| Evidence | Benign | Pathogenic |
|----------|--------|------------|
| **Population** | MAF > 5% (BA1) | Absent in controls (PS4) |
| **Computational** | BP4: No impact | PP3: Multiple algorithms predict damaging |
| **Functional** | BP5: Established benign | PS3: Well-established functional studies |
| **Segregation** | BS2: Observed in healthy | PP1: Cosegregates with disease |
| **Allelic** | BS1: MAF too high | PM3: Recessive in trans with pathogenic |

---
