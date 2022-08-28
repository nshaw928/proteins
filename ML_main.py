from utils import parse_xml, run_pisa

# General Imports
import pandas as pd



# Run PISA
pdb_file = 'C:\\Users\\nshaw\\OneDrive\\Desktop\\Projects\\proteins\\datasets\\test_results\\hbb_hba\\ranked_0.pdb'
xml_files_path = 'datasets/xml_files'
#run_pisa(pdb_file, xml_files_path)

# Get dataframe from XML file
xml_path = 'datasets/xml_files/1A3L.xml'
parse_xml(xml_path)
