#bcftools filter -i 'G5!=0 && VC="SNV" && VLD!=0 && COMMON=1' --output-type z --output dbsnp_138.b37.filtered.vcf.gz /juno/work/tempo/cmopipeline/mskcc-igenomes/igenomes/Homo_sapiens/GATK/b37/dbsnp_138.b37.vcf.gz

aws s3 --no-sign-request cp s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/b37/dbsnp_138.b37.vcf.gz .

mkdir -p intermediates
bcftools filter \
	-i 'G5!=0 && VC="SNV" && VLD!=0 && COMMON=1' \
	--output-type z \
	--output intermediates/dbsnp_138.b37.common.vcf.gz \
        dbsnp_138.b37.vcf.gz \
tabix -p vcf intermediates/dbsnp_138.b37.common.vcf.gz

bcftools filter \
	-R /juno/work/ccs/cmopipeline/forte/GRCh37/baits/idt_v2/IDT_Exome_v2_FP_b37_targets.bed \
	intermediates/dbsnp_138.b37.common.vcf.gz | \
	bcftools sort \
	--output-type z \
	--output-file intermediates/dbsnp_138.b37.common.idt_v2.vcf.gz
tabix -p vcf intermediates/dbsnp_138.b37.common.idt_v2.vcf.gz

bcftools view \
	--regions 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22 \
	--output-type z \
	--output-file intermediates/dbsnp_138.b37.common.idt_v2.autosomal.vcf.gz \
	intermediates/dbsnp_138.b37.common.idt_v2.vcf.gz

bcftools sort \
	--output-type z \
	--output-file intermediates/dbsnp_138.b37.filtered.vcf.gz \
	intermediates/dbsnp_138.b37.common.idt_v2.autosomal.vcf.gz
tabix -p vcf intermediates/dbsnp_138.b37.filtered.vcf.gz
