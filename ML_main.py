from utils import parse_xml, check_exists_by_name, run_pisa

# General Imports
import pandas as pd



# Run PISA
pdb_file = 'C:\\Users\\nshaw\\OneDrive\\Desktop\\Projects\\proteins\\datasets\\test_results\\hbb_hba\\ranked_0.pdb'
xml_files_path = 'datasets/xml_files'
run_pisa(pdb_file, xml_files_path)

