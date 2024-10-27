#!/bin/bash

# Check if a directory is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

# Directory containing FASTA files
directory="$1"

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Directory $directory does not exist."
    exit 1
fi

# Find and process each FASTA file with '.fa' or '.fasta' extension in the directory
find "$directory" -type f \( -name "*.fa" -o -name "*.fasta" \) | while IFS= read -r file; do
    # Get the base name of the file without the extension
    output_file="${file%.*}.aln"
    
    # Run MAFFT alignment command, handling special characters in filename
    echo "Running MAFFT on $(basename "$file")"
    mafft --clustalout --maxiterate 1000 --localpair "$file" > "$output_file"

    # Check if MAFFT ran successfully
    if [ $? -eq 0 ]; then
        echo "Alignment saved to $output_file"
    else
        echo "Error running MAFFT on $file"
    fi

    python new_perlplexity_clustal_alignment.py "$output_file" clustal >> aln_all_scores.txt
done
