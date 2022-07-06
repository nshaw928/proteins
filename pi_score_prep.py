# Import Packages
import pandas as pd
import os
import datetime
import shutil

# Open dataset folder and create folder to save results
os.chdir('datasets')
datasets_path = os.getcwd()
now = datetime.datetime.now()
newpath = (now.strftime("%H_%M_%m_%d_%Y"))
os.makedirs(newpath)
os.chdir(newpath)
# Creates var save_folder_path which is the path to the folder for saving our data
save_folder_path = os.getcwd()

# Create DataFrame using test data set to check for AlphaFold success or which ones need run again
pi_df = pd.DataFrame({'protA_protB': [], 'protA': [], 'protB': [], 'rank': [], 'pLDDT': []})
pi_df.head()

# Check each set of proteins to make sure the run completed, check for "ranked_0,1,2,3,4"


# Create New Dataset with only the pdb, named with proteins and total alignment error (A_B_TAE)
