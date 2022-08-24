import os


def start(af_path, protein_complex):
    # Check for data folder, and if it does not exist make it
    first_time = True
    home_path = os.getcwd()
    # Check for presence of data folder
    for item in os.listdir(home_path + '\\complexes'):
        if home_path + '\\complexes\\' + item == home_path + '\\complexes\\' + protein_complex:
            first_time = False
        else:
            pass
    # If the data folder does not exist make it and the other sub folders
    if first_time:
        os.chdir('complexes')
        os.makedirs(protein_complex)
        os.chdir(protein_complex)
        dirs = ['fasta_initial', 'fasta_result', 'alphafold_result', 'pdb_for_dropbox', 'piscore_data', 'piscore_result']
        for folder in dirs:
            os.makedirs(folder)
        os.chdir(home_path)

    # Set path variables
    data_path = home_path + '\\complexes\\' + protein_complex
    fasta_initial_path = data_path + '\\fasta_initial'
    fasta_result_path = data_path + '\\fasta_result'
    alphafold_result_path = af_path
    pdb_for_dropbox_path = data_path + '\\pdb_for_dropbox'
    piscore_data_path = data_path + '\\piscore_data'
    piscore_result_path = data_path + '\\piscore_result'

    return home_path, data_path, fasta_initial_path, fasta_result_path, alphafold_result_path, piscore_data_path, piscore_result_path, pdb_for_dropbox_path
