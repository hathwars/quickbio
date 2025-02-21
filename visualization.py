"""
Functions for visualizing biological data
"""

def sequence_logo(sequences, output_file=None):
    """
    Generate a simple ASCII sequence logo from aligned sequences
    
    Args:
        sequences (list): List of aligned sequences of equal length
        output_file (str, optional): If provided, write to this file
        
    Returns:
        str: ASCII sequence logo
    """
    if not sequences:
        return ""
        
    # Check that all sequences have the same length
    seq_length = len(sequences[0])
    if not all(len(seq) == seq_length for seq in sequences):
        raise ValueError("All sequences must have the same length")
    
    # Generate the logo
    result = []
    for pos in range(seq_length):
        # Count nucleotides at this position
        counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'U': 0, '-': 0}
        for seq in sequences:
            nucleotide = seq[pos].upper()
            if nucleotide in counts:
                counts[nucleotide] += 1
            else:
                counts['-'] += 1
                
        # Sort nucleotides by frequency
        sorted_nucs = sorted(
            [n for n in counts if counts[n] > 0],
            key=lambda n: counts[n],
            reverse=True
        )
        
        # Create a simple ASCII representation
        total = len(sequences)
        line = f"Pos {pos+1:3d}: "
        for nuc in sorted_nucs:
            freq = counts[nuc] / total
            line += f"{nuc}:{freq:.2f} "
            
        result.append(line)
    
    logo = "\n".join(result)
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write(logo)
            
    return logo

def gc_plot_data(sequence, window_size=100):
    """
    Calculate GC content across a sliding window
    
    Args:
        sequence (str): DNA sequence
        window_size (int): Size of the sliding window
        
    Returns:
        tuple: (positions, gc_values) - data points for plotting
    """
    from .dna import gc_content
    
    if len(sequence) < window_size:
        return [0], [gc_content(sequence)]
    
    positions = []
    gc_values = []
    
    for i in range(0, len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        positions.append(i + window_size // 2)
        gc_values.append(gc_content(window))
    
    return positions, gc_values