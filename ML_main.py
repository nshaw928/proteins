from utils import parse_xml, run_pisa, compile_features

# General Imports
import pandas as pd



# Run PISA
pdb_file = 'C:\\Users\\nshaw\\OneDrive\\Desktop\\Projects\\proteins\\datasets\\test_results\\hbb_hba\\ranked_0.pdb'
xml_files_path = 'datasets/xml_files'
#run_pisa(pdb_file, xml_files_path)

# Compile all xml files into single df
path_to_xml_folder = 'datasets/xml_files'
compile_features(path_to_xml_folder)
print('FINSIHED MAIN')


