"""
Functions for working with RNA sequences
"""

def validate_rna(sequence):
    """
    Validates an RNA sequence
    
    Args:
        sequence (str): RNA sequence to validate
        
    Returns:
        bool: True if sequence is valid RNA
    """
    valid_bases = set('AUGC')
    return all(base.upper() in valid_bases for base in sequence)

def complement_rna(sequence):
    """
    Get the complement of an RNA sequence
    
    Args:
        sequence (str): RNA sequence
        
    Returns:
        str: Complementary RNA sequence
    """
    if not validate_rna(sequence):
        raise ValueError("Invalid RNA sequence")
        
    complements = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complements.get(base.upper(), base) for base in sequence)

def to_dna(sequence):
    """
    Convert RNA to DNA
    
    Args:
        sequence (str): RNA sequence
        
    Returns:
        str: DNA sequence
    """
    if not validate_rna(sequence):
        raise ValueError("Invalid RNA sequence")
        
    return sequence.upper().replace('U', 'T')

def translate(sequence):
    """
    Translate RNA to protein
    
    Args:
        sequence (str): RNA sequence
        
    Returns:
        str: Amino acid sequence
    """
    if not validate_rna(sequence):
        raise ValueError("Invalid RNA sequence")
    
    # Ensure length is divisible by 3
    sequence = sequence.upper()
    remainder = len(sequence) % 3
    if remainder != 0:
        sequence = sequence[:-remainder]
    
    genetic_code = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    protein = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            amino_acid = genetic_code.get(codon, 'X')
            protein += amino_acid
    
    return protein