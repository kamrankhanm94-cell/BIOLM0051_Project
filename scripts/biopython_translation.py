from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq

def run_translation():

    base = Path("data/processed_fasta_clean")
    refs = Path("data")
    outdir = Path("data/biopython_proteins")
    outdir.mkdir(exist_ok=True)

    samples = {
        "A": "references_sampleA.fasta",
        "B": "references_sampleB.fasta",
        "D": "references_sampleD.fasta"
    }

    genetic_code = 2   # vertebrate mitochondrial code

    print("=== DNA to Protein Translation (Biopython) ===")

    for s, ref_name in samples.items():

        print("\n--- Processing Sample " + s + " ---")

        sample_file = base / ("sample" + s + ".fasta")
        ref_file = refs / ref_name
        out_file = outdir / ("sample" + s + "_with_refs.fasta")

        if not sample_file.exists():
            print("Missing input file:", sample_file)
            continue

        proteins = []

        # sample sequence
        for rec in SeqIO.parse(sample_file, "fasta"):
            seq = rec.seq.upper()
            seq = Seq(str(seq).replace("N", ""))  # remove Ns
            seq = seq[:len(seq) - (len(seq) % 3)] # trim to codon length
            prot = seq.translate(table=genetic_code, to_stop=True)
            proteins.append((rec.id + "_protein", prot))

        # reference sequences
        for rec in SeqIO.parse(ref_file, "fasta"):
            seq = rec.seq.upper()
            seq = seq[:len(seq) - (len(seq) % 3)]
            prot = seq.translate(table=genetic_code, to_stop=True)
            proteins.append((rec.id, prot))

        # write final protein FASTA
        with open(out_file, "w") as f:
            for name, prot in proteins:
                f.write(">" + name + "\n" + str(prot) + "\n")

        print("Saved:", out_file, "with", len(proteins), "protein sequences")


if __name__ == "__main__":
    run_translation()
