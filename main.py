# Import Packages
import pandas as pd
import os
import shutil
import json

# Check for datasets folder, and if it does not exist make it
first_time = True
home_path = os.getcwd()
for item in home_path:
    if home_path + '\\' + item == home_path + '\\' + 'data':
        first_time = False
    else:
        pass
if first_time:
   os.makedirs('data')
   os.chdir('data')
   dirs = ['fasta_initial', 'fasta_result', 'alphafold_result', 'piscore_data', 'piscore_result']
   for dir in dirs:
       os.makedirs(dir)

# Set path variables


# Check datasets for stage of project


# Function creates all combinations of FASTA files from one


# Function creates pdb files for PI scoring and adds rank and PLDDT scores to df


# Function adds results of PI scoring to df
