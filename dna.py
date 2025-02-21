"""
Functions for working with DNA sequences
"""

def validate_dna(sequence):
    """
    Validates a DNA sequence
    
    Args:
        sequence (str): DNA sequence to validate
        
    Returns:
        bool: True if sequence is valid DNA
    """
    valid_bases = set('ATGC')
    return all(base.upper() in valid_bases for base in sequence)

def complement_dna(sequence):
    """
    Get the complement of a DNA sequence
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        str: Complementary DNA sequence
    """
    if not validate_dna(sequence):
        raise ValueError("Invalid DNA sequence")
        
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complements.get(base.upper(), base) for base in sequence)

def reverse_complement(sequence):
    """
    Get the reverse complement of a DNA sequence
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        str: Reverse complementary DNA sequence
    """
    return complement_dna(sequence)[::-1]

def gc_content(sequence):
    """
    Calculate the GC content of a DNA sequence
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        float: GC content as a decimal (0-1)
    """
    if not sequence:
        return 0
        
    sequence = sequence.upper()
    return (sequence.count('G') + sequence.count('C')) / len(sequence)

def transcribe(sequence):
    """
    Transcribe DNA to RNA
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        str: RNA sequence
    """
    if not validate_dna(sequence):
        raise ValueError("Invalid DNA sequence")
        
    return sequence.upper().replace('T', 'U')