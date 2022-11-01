from utils import run_pisa, parse_xml, compile_features

# General Imports
import pandas as pd
import os

test_xml = 'data/117e_outfile'

parse_xml(test_xml)







# Run PISA
pdb_folder = 'D:\\Data\\Aug26_PDB'
xml_files_path = 'data/xml_files/Sep7'

#for file in os.listdir(pdb_folder):
#    file_name = pdb_folder + '\\' + file
#    run_pisa(file_name, xml_files_path)

# Compile all xml files into single df
#path_to_xml_folder = 'datasets/xml_files'
#compile_features(path_to_xml_folder)
print('FINSIHED MAIN')


