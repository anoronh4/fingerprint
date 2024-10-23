from __future__ import print_function
import pysam
counter = 0
input = "dbsnp_138.b37.filtered.vcf.gz"
vcf_in = pysam.VariantFile(input, "r")
out_vcf = open("dbsnp_138.b37.filtered.idt_v2.caf_filter.vcf", 'w')
print(vcf_in.header, end="", file=out_vcf)


for vcf_rec in vcf_in.fetch():
    counter +=1
    if not "CAF" in vcf_rec.info.keys():
        continue
    try:
        AF_left = float(vcf_rec.info["CAF"][0].replace("[","").replace("]",""))
        AF_right = float(vcf_rec.info["CAF"][1].replace("[","").replace("]",""))
        if AF_left > .70 or AF_right > .70:
            pass
        else:
            print(vcf_rec, end="", file=out_vcf)
    except:
        pass
    

out_vcf.close()
