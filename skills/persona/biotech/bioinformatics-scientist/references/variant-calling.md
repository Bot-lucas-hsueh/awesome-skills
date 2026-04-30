# 6. Variant Calling
gatk HaplotypeCaller -I sample.recal.bam -R ref.fa -O sample.g.vcf.gz -ERC GVCF
gatk GenotypeGVCFs -R ref.fa -V sample.g.vcf.gz -O sample.vcf.gz
