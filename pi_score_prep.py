# Import Packages
import pandas as pd
import os
import datetime
import shutil

# Open dataset folder and create folder to save results
os.chdir('datasets')
datasets_path = os.getcwd()

# Save path to folder for copying our ranked pdbs
now = datetime.datetime.now()
newpath = (now.strftime("%H_%M_%m_%d_%Y"))
os.makedirs(newpath)
os.chdir(newpath)
save_folder_path = os.getcwd()

# Save path to folder of AlphaFold result folders
os.chdir(datasets_path)
os.chdir('test_results')
results_data_path = os.getcwd()

# Save path to folder of FASTA files
os.chdir(datasets_path)
os.chdir('test_data')
fasta_data_path = os.getcwd()

# Create DataFrame using test data set to check for AlphaFold success or which ones need run again
pi_df = pd.DataFrame({'protA_protB': [], 'protA': [], 'protB': [], 'rank': [], 'pLDDT': []})

# Populate protA_protB, protA, and protB from the fasta files
for file in os.listdir(fasta_data_path):
    # Save file name as string
    filename = file
    # Get rid of .fasta

    # Save protA_protB to df

    # Separate protA and protB and save to df


# Check each set of proteins to make sure the run completed, check for "ranked_0,1,2,3,4"


# Create New Dataset with only the pdb, named with proteins and total alignment error (A_B_TAE)
