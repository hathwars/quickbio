"""
QuickBio: A lightweight bioinformatics toolkit for DNA/RNA sequence analysis
"""

__version__ = '0.1.0'

from .dna import (
    complement_dna, # complement DNA sequence
    reverse_complement, # reverse complement DNA sequence
    gc_content, # calculate GC content
    transcribe # transcribe DNA to RNA
)

from .rna import (
    complement_rna, # complement RNA sequence       
    to_dna, # convert RNA to DNA
    translate # translate RNA to protein
)

from .utils import (
    read_fasta, # read sequences from a FASTA file
    write_fasta,
    validate_sequence
)