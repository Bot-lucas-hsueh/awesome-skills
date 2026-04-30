# 3. Alignment
bwa mem -t 8 -R "@RG\tID:sample\tSM:sample\tPL:ILLUMINA" \
  ref.fa sample_R1_val_1.fq.gz sample_R2_val_2.fq.gz | \
  samtools sort -@ 4 -o sample.sorted.bam -
