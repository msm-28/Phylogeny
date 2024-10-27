import sys
from Bio import AlignIO

def calculate_alignment_score(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-2):
    """
    Calculate the alignment score between two sequences.
    
    Parameters:
        seq1 (str): The first sequence.
        seq2 (str): The second sequence.
        match_score (int): Score for matching characters.
        mismatch_penalty (int): Penalty for mismatching characters.
        gap_penalty (int): Penalty for introducing gaps.
        
    Returns:
        int: The total alignment score.
    """
    total_score = 0
    len1 = len(seq1)
    len2 = len(seq2)
    #print(len1,len2)
    for i in range(max(len1, len2)):
        char1 = seq1[i] if i < len1 else '-'
        char2 = seq2[i] if i < len2 else '-'
        
        if char1 == '-' or char2 == '-':
            total_score += gap_penalty
            #print(gap_penalty)
        elif char1 == char2:
            total_score += match_score
            #print(match_score)
        else:
            total_score += mismatch_penalty
            #print(mismatch_penalty)
            
    return total_score

def main():
    # Check if the user provided a filename and format
    if len(sys.argv) != 3:
        print("Usage: python script.py <alignment_file> <file_format>")
        sys.exit(1)

    # Get the filename and format from command line arguments
    alignment_file = sys.argv[1]
    file_format = sys.argv[2]

    try:
        # Read the alignment file
        alignment = AlignIO.read(alignment_file, file_format)

        # Calculate and print scores for each pair of sequences
        num_sequences = len(alignment)
        #print(num_sequences)
        
        #print("Alignment Scores:")
        
        for i in range(num_sequences):
            for j in range(i + 1, num_sequences):
                seq1 = str(alignment[i].seq)
                seq2 = str(alignment[j].seq)

                sl1 = len(seq1)
                sl2 = len(seq2)
                #print(seq1, seq2)
                score = calculate_alignment_score(seq1, seq2)
                print(f"Score between {alignment[i].id} and {alignment[j].id}: {score}")

    except Exception as e:
        print(f"Error reading alignment file: {e}")

if __name__ == "__main__":
    main()
