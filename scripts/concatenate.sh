#!/bin/bash
echo "=== FASTQ to FASTA Conversion ==="

# Input and output directories
INPUT_DIR="data/samples"
OUTPUT_DIR="data/processed_fasta"

# Create output directory
mkdir -p $OUTPUT_DIR

# Process each sample
for sample in A B C D; do
    echo "Processing sample $sample..."
    
    # Concatenate all parts and convert to FASTA
    cat $INPUT_DIR/sample${sample}_part1.FASTQ \
        $INPUT_DIR/sample${sample}_part2.FASTQ \
        $INPUT_DIR/sample${sample}_part3.FASTQ | \
    awk 'NR%4==1 {print ">" substr($0,2)} NR%4==2 {print}' > \
    $OUTPUT_DIR/sample${sample}.fasta
    
    echo "Sample $sample done: $OUTPUT_DIR/sample${sample}.fasta"
done

echo "=== All samples converted successfully ==="