# 4. Post-processing
samtools index sample.sorted.bam
picard MarkDuplicates -I sample.sorted.bam -O sample.dedup.bam -M metrics.txt
samtools index sample.dedup.bam
