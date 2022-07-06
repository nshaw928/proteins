# Import Packages
import pandas as pd
import os
import datetime
import shutil
import json

# Create new folder for saving results and save paths to relevant datasets
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
    # Save strings to be used in the df
    protA_protB = filename.split('.')[0]
    protA = protA_protB.split('_')[0]
    protB = protA_protB.split('_')[1]
    # Create dict with prot names and add to pi_df
    temp_dict = {'protA_protB': protA_protB, 'protA': protA, 'protB': protB}
    temp_df = pd.DataFrame([temp_dict])
    pi_df = pd.concat([pi_df, temp_df], ignore_index=True)

# Saved ranked pdbs in new folder with name protA_protB_#.pdb (created earlier)
for folder in os.listdir(results_data_path):
    if os.path.exists(results_data_path + '\\' + folder + '\\ranked_0.pdb'):
        shutil.copyfile(results_data_path + '\\' + folder + '\\ranked_0.pdb', save_folder_path + '\\ranked_0.pdb')
        new_file_name = '\\' + folder + '_0.pdb'
        os.rename(save_folder_path + '\\ranked_0.pdb', save_folder_path + new_file_name)
    if os.path.exists(results_data_path + '\\' + folder + '\\ranked_1.pdb'):
        shutil.copyfile(results_data_path + '\\' + folder + '\\ranked_1.pdb', save_folder_path + '\\ranked_1.pdb')
        new_file_name = '\\' + folder + '_1.pdb'
        os.rename(save_folder_path + '\\ranked_1.pdb', save_folder_path + new_file_name)
    if os.path.exists(results_data_path + '\\' + folder + '\\ranked_2.pdb'):
        shutil.copyfile(results_data_path + '\\' + folder + '\\ranked_2.pdb', save_folder_path + '\\ranked_2.pdb')
        new_file_name = '\\' + folder + '_2.pdb'
        os.rename(save_folder_path + '\\ranked_2.pdb', save_folder_path + new_file_name)
    if os.path.exists(results_data_path + '\\' + folder + '\\ranked_3.pdb'):
        shutil.copyfile(results_data_path + '\\' + folder + '\\ranked_3.pdb', save_folder_path + '\\ranked_3.pdb')
        new_file_name = '\\' + folder + '_3.pdb'
        os.rename(save_folder_path + '\\ranked_3.pdb', save_folder_path + new_file_name)
    if os.path.exists(results_data_path + '\\' + folder + '\\ranked_4.pdb'):
        shutil.copyfile(results_data_path + '\\' + folder + '\\ranked_4.pdb', save_folder_path + '\\ranked_4.pdb')
        new_file_name = '\\' + folder + '_4.pdb'
        os.rename(save_folder_path + '\\ranked_4.pdb', save_folder_path + new_file_name)
    else:
        pass

# Update pi_df with rankings for each protein set and their pLDDT score
# Add rows to pi_df for each rank of protein
print(pi_df.head())

#
