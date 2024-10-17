sample=$1
bam=$(readlink -f $2)
normal=$3
normalbam=$4
outdir=$5
fasta=$6
variant_input=$7
#    fasta=/juno/work/tempo/cmopipeline/mskcc-igenomes/igenomes/Homo_sapiens/NCBI/GRCh38Decoy/Sequence/WholeGenomeFasta/genome.fa
#    fasta=/juno/work/ci/resources/genomes/GRCh37/fasta/b37.fasta
#variant_input=/juno/work/ccs/noronhaa/tools/fingerprint/FP.vcf
output=$sample.vcf

singularity exec -e --no-home -B $outdir -B $(dirname $fasta) -B $(dirname $bam) -B $(dirname $normalbam) -B $(dirname $variant_input) docker://ghcr.io/msk-access/gbcms:1.2.5 \
GetBaseCountsMultiSample \
     --maq 0 \
	--fasta ${fasta} \
    --vcf ${variant_input} \
        --output $outdir/${output} \
	    --bam $sample:${bam} \
            --bam $normal:${normalbam}
