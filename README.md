# fingerprint

How to run
```
bash gbcms.sh $sample_id /path/to/sample.bam result/ /path/to/fasta /path/to/FP.vcf
python ./parse_fingerprint_vcf.py --input result/$sample_id.vcf --samplename $sample_id --output result/$sample_id.fp.txt
```
