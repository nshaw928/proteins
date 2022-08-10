from start import start
from generate_fasta import generate_fasta
from generate_pdbs_from_af import generate_pdbs_from_af
from extract_piscore import extract_piscore

# Set which protein complex you are working on
protein_complex = '139_IFTB'
af = 'F:\\alphafold_data\\p139_IFTB_result'

# Run start function to create folders and set save paths
home_path, data_path, fasta_initial_path, fasta_result_path, alphafold_result_path, piscore_data_path,\
    piscore_result_path, pdb_for_dropbox = start(af_path=af, protein_complex=protein_complex)

# Run generate_fasta function to generate fasta files to be used as AlphaFold input
generate_fasta(run_type='1_with_all', home_path=home_path, data_path=data_path, fasta_initial_path=fasta_initial_path,
               fasta_result_path=fasta_result_path)

# Saves the top ranked alphafold prediction for pi scoring as index for associated interaction from pre_piscore.csv
generate_pdbs_from_af(fasta_result_path=fasta_result_path, alphafold_result_path=alphafold_result_path,
                      piscore_data_path=piscore_data_path, data_path=data_path, pdb_for_dropbox=pdb_for_dropbox)

# Extracts pi score from the results of pi score program
#extract_piscore(data_path=data_path, piscore_result_path=piscore_result_path)
