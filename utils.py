import pandas as pd
import os
import time
import xml.etree.ElementTree as ET


# Designed to run PISA from the linux command line installed through CCP4
def run_pisa(path_to_data_folder):

    # Specify where you want the results to go
    result_path = '/home/nshaw928/Documents/results/Aug26_PDB/'

    # Navigate to correct path
    os.chdir('/opt/xtal/ccp4-8.0')
    print(os.getcwd())
    os.system('bin/ccp4.setup-sh')

    for file in os.listdir(path_to_data_folder):
        os.system('/opt/xtal/ccp4-8.0/bin/pisa name -analyse ' + file)
        output_file_path = result_path + file.split('.')[0] + '_pisa.xml'
        os.system('pisa name -xml interfaces >' + output_file_path)
        os.system('pisa name -erase')

# NEW PARSE FUNCTION
def parse_xml(path_to_xml):
    # Save the name of the proteins
    proteinA = path_to_xml.split('_')[0]
    proteinB = path_to_xml.split('_')[1]
    proteins = proteinA + '_' + proteinB

    # Load the xml file into the parse system
    tree = ET.parse(path_to_xml)
    root = tree.getroot()

    # Define a dataframe to save the interface to
    df = pd.DataFrame({
        'area': [],
        'deltag': [],
        'pvalue': [],
        'hbonds': [],
        'saltbridges': [],
        'tot_res': [],
    })

    # Separate each interface and extract features
    for interface in root.findall('interface'):
        area = interface.find('int_area').text
        deltag = interface.find('int_solv_en').text
        pvalue = interface.find('pvalue').text

        # Save the number of each type of interaction as a var
        for hbond in interface.findall('h-bonds'):
            hbonds = int(hbond.find('n_bonds').text)
        for saltbridge in interface.findall('salt-bridges'):
            saltbridges = int(saltbridge.find('n_bonds').text)

        # Save the number of residues from each molecule
        counter = 0
        for molecule in interface.findall('molecule'):
            if counter == 0:
                chain1_res = int(molecule.find('int_nres').text)
                counter += 1
            else:
                chain2_res = int(molecule.find('int_nres').text)

        # Save all for this particular interface into a temporary df
        temp_df = pd.DataFrame({
        'area': [area],
        'deltag': [deltag],
        'pvalue': [pvalue],
        'hbonds': [hbonds],
        'saltbridges': [saltbridges],
        'tot_res': [(chain1_res + chain2_res)],
        })

        # Append the temporary df to the main one
        df = pd.concat([df, temp_df])

    # Filters out small interfaces
    df = df[df['tot_res'] > 2]

    # Converts columns to floats for compatability
    df['area'] = df['area'].astype(float)
    df['deltag'] = df['deltag'].astype(float)
    df['pvalue'] = df['pvalue'].astype(float)

    # Summarize the interface data into a single row
    # Save summaries of features as vars
    sum_hbonds = df['hbonds'].sum()
    sum_saltbridges = df['saltbridges'].sum()
    sum_area = df['area'].sum()
    sum_tot_res = df['tot_res'].sum()
    sum_deltag = df['deltag'].sum()

    # Summarize df in single row of new_df
    summary_df = pd.DataFrame({
        'protA_protB': [proteins],
        'hbonds': [sum_hbonds],
        'saltbridges': [sum_saltbridges],
        'area': [sum_area],
        'deltag': [sum_deltag],
        'tot_res': [sum_tot_res],
    })

    # Returns new_df which is a single row summarizing the interaction
    return summary_df

# Compile features from all xml files (uses function parse_xml)
def compile_features(path_to_xml_folder):
    # Define the master df that all interactions will be saved in
    df_final = pd.DataFrame({
        'protA_protB': [],
        'hbonds': [],
        'saltbridges': [],
        'area': [],
        'deltag': [],
        'tot_res': [],
    })

    # Loops that goes through the folder with xml files and passes each file to parse_xml
    for file in os.listdir(path_to_xml_folder):
        # Save the full path to the file
        file_path = path_to_xml_folder + '/' + file

        # Run parse_xml and save to temp_df
        temp_df = parse_xml(file_path)

        # Add temp_df to the master df, df
        df_final = pd.concat([df_final, temp_df])

    print('FINISH')