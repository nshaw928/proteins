# Import Packages
import pandas as pd
import os
import datetime
import shutil

# Open dataset folder and create folder to save results
os.chdir('datasets')
datasets_path = os.getcwd()

# Save path to folder for copying our ranked pdbs
#now = datetime.datetime.now()
#newpath = (now.strftime("%H_%M_%m_%d_%Y"))
#os.makedirs(newpath)
#os.chdir(newpath)
#save_folder_path = os.getcwd()

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
    # Save strings to be used in the df
    protA_protB = filename.split('.')[0]
    protA = protA_protB.split('_')[0]
    protB = protA_protB.split('_')[1]
    # Create dict with prot names and add to pi_df
    temp_dict = {'protA_protB': protA_protB, 'protA': protA, 'protB': protB}
    temp_df = pd.DataFrame([temp_dict])
    pi_df = pd.concat([pi_df, temp_df], ignore_index=True)\
print(pi_df.head())

# Check each set of proteins to make sure the run completed, check for "ranked_0,1,2,3,4"


# Create New Dataset with only the pdb, named with proteins and total alignment error (A_B_TAE)
