# BIOLM0051 – DNA Barcoding & Phylogenetic Analysis Project  
**Author**: Mohd Kamran Khan  
**Module:** BIOLM0051  

---

##  Project Overview

This repository contains all data, scripts, alignments and phylogenetic trees created for the BIOLM0051 coursework.

The aims of the project were to:

1. Clean and process FASTQ files  
2. Convert merged reads into FASTA  
3. Translate DNA sequences into amino acids using **Biopython** (Translation Table 2)  
4. Perform **multiple sequence alignment (MSA)** using **Clustal Omega**  
5. Construct **phylogenetic trees** using **EBI Simple Phylogeny**  
6. Identify the likely species origins of three unknown samples (**Sample A, Sample B, Sample D**)

>  Note: Sample C contained corrupted sequence data (too many ambiguous “N” bases and formatting errors) and was excluded from downstream analysis.

---

Repository Structure

```text
BIOLM0051_Project/
│
├── data/
│   ├── samples/                  # Raw FASTQ files (SampleA–D)
│   ├── combined/                 # Merged FASTQ files
│   ├── processed_fasta/          # Clean FASTA sequences
│   ├── processed_fasta_clean/    # Additional cleaned FASTA
│   ├── references_sampleA.fasta  # Reference sequences for Sample A
│   ├── references_sampleB.fasta  # Reference sequences for Sample B
│   ├── references_sampleD.fasta  # Reference sequences for Sample D
│   └── biopython_proteins/       # DNA→Protein translations (with references)
│
├── results/
│   ├── alignment/                # Clustal Omega MSA outputs
│   └── trees/                    # Phylogenetic trees (.nwk + PNG)
│
├── scripts/
│   ├── concatenate.sh            # Merge FASTQ parts for each sample
│   ├── clean_convert.py          # Clean + convert FASTQ → FASTA
│   ├── convert_properly.sh       # Helper for FASTQ→FASTA (alternative)
│   └── biopython_translation.py  # Translate DNA → protein with Biopython
│
├── documentation/
│   └── BIOLM0051_Report_MohdKamranKhan.pdf   # Final written report
│
└── README.md


---

## How to Reproduce the Analysis

### 1. Merge paired FASTQ files  

### 2. Clean FASTQ & convert to FASTA  

### 3. Translate DNA to protein  

### 4. Run multiple sequence alignment  
Uploaded FASTA files were aligned on **EMBL-EBI Clustal Omega**.

### 5. Build phylogenetic trees  
Aligned files sent to **EMBL-EBI Simple Phylogeny**.

---

## Supplementary Materials

 **Full Report (PDF):**  
documentation/BIOLM0051_Report_MohdKamranKhan.pdf

 **GitHub Repository Link:**  
https://github.com/kamrankhanm94-cell/BIOLM0051_Project

---

## Tools & Software Used

- **Biopython 1.86**  
- **Clustal Omega (EBI Webserver)**  
- **Simple Phylogeny (EBI Webserver)**  
- **NCBI BLAST**  
- **Python 3.10+**  
- **Git + GitHub**

---

## Acknowledgements
This pipeline was completed as part of the BIOLM0051 module at the University of Bedfordshire.



