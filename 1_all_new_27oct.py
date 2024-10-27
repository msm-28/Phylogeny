import re
from itertools import combinations

def read_multifasta(multi_fasta_file):
    sequences = {}
    with open(multi_fasta_file, "r") as file:
        seq_id = None
        seq = []
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if seq_id is not None:
                    sequences[seq_id] = ''.join(seq)
                # Extract the specific identifier using regex (P02216|GLB1_GLYDI)
                seq_id_full = line[1:]  # Skip the '>'
                match = re.search(r"\|([A-Z0-9]+?\|[A-Z0-9_]+)\s", seq_id_full)
                if match:
                    seq_id = match.group(1)
                    print(f"Extracted Identifier: {seq_id}")  # Debug print
                seq = []
            else:
                seq.append(line)
        if seq_id is not None:
            sequences[seq_id] = ''.join(seq)  # Save the last sequence
    return sequences

def write_pairwise_combinations(sequences):
    with open("output_filenames.log", "w") as log_file:  # Open the log file to write filenames
        for (id1, seq1), (id2, seq2) in combinations(sequences.items(), 2):
            # Create the filename with the full seq_ids
            filename = f"{id1}_{id2}.fasta"
            print(filename)
            #print(filename)
            with open(filename, "w") as outfile:
                outfile.write(f">{id1}\n{seq1}\n")
                #print(len(seq1))
                outfile.write(f">{id2}\n{seq2}\n")
                #print(len(seq2))
            # Record the filename in the log file
            log_file.write(f"{filename}: {len(seq1)}: {len(seq2)}\n")

def main(multi_fasta_file):
    sequences = read_multifasta(multi_fasta_file)
    write_pairwise_combinations(sequences)

# Example usage
if __name__ == "__main__":
    multi_fasta_file = "glycera_all.fasta"  # Replace with your file path
    main(multi_fasta_file)

