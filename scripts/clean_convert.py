from Bio import SeqIO
from pathlib import Path
import re

input_dir = Path("data/samples")
output_dir = Path("data/processed_fasta_clean")
output_dir.mkdir(exist_ok=True)

samples = ["A", "B", "C", "D"]

def clean_sequence(seq):
    # Remove whitespace and invalid characters
    seq = re.sub(r"\s+", "", seq)         # remove whitespace
    seq = seq.upper()
    seq = re.sub(r"[^ATCGN]", "N", seq)   # replace invalid chars with N
    return seq

for s in samples:
    parts = [
        input_dir / f"sample{s}_part1.FASTQ",
        input_dir / f"sample{s}_part2.FASTQ",
        input_dir / f"sample{s}_part3.FASTQ",
    ]

    clean_records = []
    for part in parts:
        try:
            for rec in SeqIO.parse(part, "fastq"):
                seq_str = str(rec.seq)
                seq_clean = clean_sequence(seq_str)

                rec.seq = seq_clean
                rec.letter_annotations = {}
                clean_records.append(rec)
        except Exception as e:
            print(f"Skipping corrupted file part: {part} ({e})")

    out_fasta = output_dir / f"sample{s}.fasta"
    SeqIO.write(clean_records, out_fasta, "fasta")
    print(f"Clean FASTA saved: {out_fasta}")
