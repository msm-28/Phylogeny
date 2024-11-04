from Bio import SeqIO

def format_sequence(sequence, line_length=60):
    """Format the sequence into lines of specified length."""
    return '\n'.join(sequence[i:i + line_length] for i in range(0, len(sequence), line_length))

def extract_identifiers_and_sequences(fasta_file):
    """Extract identifiers and sequences from a multi-FASTA file."""
    with open(fasta_file, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            # Extract identifier and sequence
            full_identifier = record.id  # Get the identifier
            identifier = full_identifier.split('|')[2] if '|' in full_identifier else full_identifier
            sequence = str(record.seq)  # Get the sequence as a string
            
            # Format the sequence to 60 characters per line
            formatted_sequence = format_sequence(sequence)
            
            # Print formatted output
            print(f">{identifier}")
            print(formatted_sequence)

if __name__ == "__main__":
    # Specify your multi-FASTA file path
    fasta_file_path = "/home/madhura/Documents/Phylogeny/All_sequences_tree_4Nov2024/idmapping_2024_11_04.fasta"
    extract_identifiers_and_sequences(fasta_file_path)
