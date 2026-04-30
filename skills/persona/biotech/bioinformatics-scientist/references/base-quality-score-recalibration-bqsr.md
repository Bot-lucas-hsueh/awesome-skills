# 5. Base Quality Score Recalibration (BQSR)
gatk BaseRecalibrator -I sample.dedup.bam -R ref.fa --known-sites dbsnp.vcf -O recal.table
gatk ApplyBQSR -I sample.dedup.bam -R ref.fa --bqsr-recal-file recal.table -O sample.recal.bam
