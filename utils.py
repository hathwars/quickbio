"""
Utility functions for bioinformatics operations
"""

def validate_sequence(sequence, seq_type='dna'):
    """
    Validate a biological sequence
    
    Args:
        sequence (str): Sequence to validate
        seq_type (str): Type of sequence ('dna', 'rna', or 'protein')
        
    Returns:
        bool: True if valid sequence
    """
    seq_type = seq_type.lower()
    sequence = sequence.upper()
    
    if seq_type == 'dna':
        valid_chars = set('ATGC')
    elif seq_type == 'rna':
        valid_chars = set('AUGC')
    elif seq_type == 'protein':
        valid_chars = set('ACDEFGHIKLMNPQRSTVWY*')
    else:
        raise ValueError(f"Unknown sequence type: {seq_type}")
        
    return all(char in valid_chars for char in sequence)

def read_fasta(filename):
    """
    Read sequences from a FASTA file
    
    Args:
        filename (str): Path to FASTA file
        
    Returns:
        dict: Dictionary mapping sequence IDs to sequences
    """
    sequences = {}
    current_id = None
    current_seq = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('>'):
                # Save the previous sequence if it exists
                if current_id:
                    sequences[current_id] = ''.join(current_seq)
                
                # Start a new sequence
                current_id = line[1:].split()[0]  # Get ID without description
                current_seq = []
            else:
                current_seq.append(line)
    
    # Save the last sequence
    if current_id:
        sequences[current_id] = ''.join(current_seq)
    
    return sequences

def write_fasta(sequences, filename):
    """
    Write sequences to a FASTA file
    
    Args:
        sequences (dict): Dictionary mapping sequence IDs to sequences
        filename (str): Output filename
    """
    with open(filename, 'w') as f:
        for seq_id, sequence in sequences.items():
            f.write(f">{seq_id}\n")
            
            # Write sequence in chunks of 80 characters
            for i in range(0, len(sequence), 80):
                f.write(sequence[i:i+80] + "\n")