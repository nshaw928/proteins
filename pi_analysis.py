# Import packages
import pandas as pd
import os

# Get paths for necessary folders
os.chdir('datasets')
datasets_path = os.getcwd()
# Save path for PI score results
os.chdir(datasets_path + '\\piscore_result')
piscore_result_path = os.getcwd()

# Get df


# Add features from PI scoring to df
for folder in os.listdir(piscore_result_path):
    for item in os.listdir(piscore_result_path + '\\' + folder):
        temp_path = piscore_result_path + '\\' + folder
        isdir = os.path.isdir(temp_path + '\\' + item)
        if isdir:
            for thing in os.listdir(piscore_result_path + '\\' + folder + '\\' + item):
                temp_path = piscore_result_path + '\\' + folder + '\\' + item
                isdir = os.path.isdir(temp_path + '\\' + thing)
                if isdir:
                    print(temp_path + '\\' + thing)
        else:
            pass

# Add PI score and class
