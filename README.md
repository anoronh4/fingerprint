# fingerprint

# Paired samples

```
bash gbcms_paired.sh tumor_id /path/to/tumor.bam normal_id /path/to/normal.bam result/ /path/to/fasta /path/to/FP.vcf
python ./parse_fingerprint_vcf.py --input result/$tumor_id.vcf --samplename $tumor_id --normalname $normal_id --output result/$tumor_id.fp.txt
python ./parse_fingerprint_vcf.py --input result/$tumor_id.vcf --samplename $normal_id --output result/$tumor_id.fp.txt

```

# Unpaired samples
```
bash gbcms.sh $sample_id /path/to/sample.bam result/ /path/to/fasta /path/to/FP.vcf
python ./parse_fingerprint_vcf.py --input result/$sample_id.vcf --output result/$sample_id.fp.txt
```
