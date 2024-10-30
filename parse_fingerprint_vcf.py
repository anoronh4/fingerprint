import argparse

"""
Perform custom filtering/annotation of variants in 
VCF file, after merging SVs with mergesvvcf. Variants
with a minimum of PASSing callers should be filtered 
as PASS with all non-PASS filters recorded in INFO.
Additionally, TRA is converted to BND because svtools
will not correctly handle TRA.
Usage: filter-sv-vcf.py -h 
"""

__author__  = "Anne Marie Noronha"
__email__   = "noronhaa@mskcc.org"
__version__ = "0.0.1"
__status__  = "Dev"

import sys, os
from pysam import VariantFile    # version >= 0.15.2
from itertools import groupby

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help = 'input file', required = True)
    parser.add_argument('--samplename', help = 'sample name', required = True)
    parser.add_argument('--output', help = 'output file', required = True)
    return parser.parse_args()

def main():
    args = usage()

    fp_out_list = []

    vcf_in = VariantFile(args.input, "r")
    for vcf_rec in vcf_in.fetch():
        ref_allele = vcf_rec.ref
        alt_allele = vcf_rec.alts[0]
        ref_allele_count = vcf_rec.samples[args.samplename]["RD"]
        alt_allele_count = vcf_rec.samples[args.samplename]["AD"]
        if ref_allele_count >= alt_allele_count and ref_allele_count > 0:
            if alt_allele_count < .1 * ref_allele_count:
                genotype = ref_allele*2
            else: genotype = ref_allele + alt_allele
            maf = alt_allele_count / float(ref_allele_count + alt_allele_count)
        elif alt_allele_count > ref_allele_count:
            if ref_allele_count < .1 * alt_allele_count:
                genotype = alt_allele*2
            else: genotype = ref_allele + alt_allele 
            maf = ref_allele_count / float(ref_allele_count + alt_allele_count)
        elif ref_allele_count == 0: genotype = "--"
        else: genotype = ref_allele + alt_allele
        if ref_allele_count + alt_allele_count < 20 or genotype == "--":
            maf = ""


        formatted_counts = "{}:{} {}:{}".format(ref_allele,ref_allele_count,alt_allele,alt_allele_count)

        locus = "{}:{}".format(vcf_rec.chrom,vcf_rec.pos)
        depth = vcf_rec.samples[args.samplename]["DP"]

        fp_out_list += [[locus,formatted_counts, genotype, maf, depth]]

    with open(args.output,'w') as f:
        f.write("\t".join(['Locus', args.samplename + '_Counts', args.samplename + '_Genotypes', args.samplename + '_MinorAlleleFreq', args.samplename + '_Depth']) + "\n")
        for i in fp_out_list:
            f.write("\t".join([str(j) for j in i]) + "\n")

if __name__ == "__main__":
    main()
