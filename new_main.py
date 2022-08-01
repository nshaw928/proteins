from start import start
from generate_fasta import generate_fasta

# Set which protein complex you are working on
protein_complex = 'zync_finger_with_IFTB'

# Run start function to create folders and set save paths
home_path, data_path, fasta_initial_path, fasta_result_path, alphafold_result_path, piscore_data_path,\
    piscore_result_path = start(af_path='F:\\alphafold_data\\CytC_result', protein_complex=protein_complex)

# Run generate_fasta function to generate fasta files to be used as AlphaFold input
generate_fasta(run_type='1_with_all', home_path=home_path, data_path=data_path, fasta_initial_path=fasta_initial_path,
               fasta_result_path=fasta_result_path)
