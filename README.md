# All the scripts relevant to my work on phylogeny are stored in this repository
mafft --clustalout --maxiterate 1000 --localpair idmapping_2024_11_04_reformatted_removed_dicde_artsx.fasta > idmapping_2024_11_04_reformatted_removed_dicde_artsx.aln

./iqtree2 -s /home/madhura/Documents/Phylogeny/All_sequences_tree_4Nov2024/idmapping_2024_11_04_reformatted_removed_dicde_artsx.aln -st AA -m TEST -bb 1000 -alrt 1000
