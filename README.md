# QuickBio

A lightweight Python package for common bioinformatics tasks.

## Features

* DNA and RNA sequence manipulation
* Sequence validation
* GC content calculation
* Transcription and translation
* FASTA file handling
* Basic sequence visualization

## Installation

```bash
pip install quickbio
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/yourusername/quickbio.git
```

## Usage Examples

```python
import quickbio

# Basic DNA operations
dna_seq = "ATGCGATCGATCGATCG"
print(f"GC content: {quickbio.gc_content(dna_seq)}")
print(f"Reverse complement: {quickbio.reverse_complement(dna_seq)}")

# Transcription and translation
rna_seq = quickbio.transcribe(dna_seq)
print(f"RNA: {rna_seq}")
protein = quickbio.translate(rna_seq)
print(f"Protein: {protein}")

# Working with FASTA files
sequences = quickbio.read_fasta("sequences.fasta")
for seq_id, sequence in sequences.items():
    print(f"Sequence {seq_id} is {len(sequence)} bp long")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.