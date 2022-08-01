import pandas as pd
import os


def parse_fasta(fasta_file, data_path):
    '''
    :param data_path: path to data folder for the protein complex
    :param fasta_file: fasta file to be loaded by generate_fasta() function
    :return: outputs a csv titled proteins.csv in the data_path directory
    '''
    # Define variables for use later
    sequences_dict = {}
    temp_sequences_dict = {}
    temp_seq_id = None
    temp_seq = []

    # Creates a dictionary containing key (Uniprot Information) and value (AA sequence)
    for line in fasta_file:
        line = line.strip()
        if line.startswith(">"):
            if temp_seq_id is not None:
                sequences_dict[temp_seq_id] = ''.join(temp_seq)
            temp_seq_id = line[1:]
            temp_seq = []
            continue
        temp_seq.append(line)
    sequences_dict[temp_seq_id] = ''.join(temp_seq)

    # Simplifies the key of the dictionary to only be the 6 digit UniProt-ID
    for key, value in sequences_dict.items():
        temp_key = key
        temp_key = temp_key.split()
        temp_key = temp_key[0]
        temp_key = temp_key.split("|")
        temp_key = temp_key[1]
        temp_sequences_dict[temp_key] = value

    # Save over the previous dictionary with the messy keys to our one with the simplified keys
    sequences_dict = temp_sequences_dict

    # Define the DataFrame that our sequence data will be stored in
    df = pd.DataFrame({'id': [], 'sequence': [], })

    # Fill DataFrame with our data
    for key, value in sequences_dict.items():
        temp_dict = {'id': key, 'sequence': value}
        df = df.append(temp_dict, ignore_index=True)

    # Adds sequence_length column
    df['sequence_length'] = df['sequence'].str.len()

    # Save df as CSV
    df.to_csv(data_path + '\\proteins.csv')
    return df


def write_fasta(data_dict, dimers=False):
    # Sets file name and opens the file for modification
    file_name = []
    for key, value in data_dict.items():
        file_name.append(key)
        if dimers and len(data_dict) == 1:
            file_name.append(key)
    file_name = '_'.join(file_name)
    output_path = file_name + '.fasta'
    output_file = open(output_path, 'w')

    # Modifying the output file, adding the identifier lines and sequences
    for key, value in data_dict.items():
        identifier_line = ">" + key + "\n"
        output_file.write(identifier_line)
        sequence_line = value + '\n'
        output_file.write(sequence_line)
        # This is for if you want to generate FASTA files for prediction of dimers as well,
        # the value can be changed to true when calling the function
        if dimers and len(data_dict) == 1:
            identifier_line = ">" + key + "\n"
            output_file.write(identifier_line)
            sequence_line = value + '\n'
            output_file.write(sequence_line)

    # Closes the file, ending editing
    output_file.close()


def all_pairs(dataframe):
    '''
    Generates all pairs of proteins possible from given dataframe
    :param dataframe: dataframe containing id and sequence information
    :return: outputs fasta
    '''
    count = 0
    # Loops through all proteins in dataframe
    for first_element_index in range(0, len(dataframe)):
        first_element = {dataframe.loc[first_element_index, 'id']: dataframe.loc[first_element_index, 'sequence']}
        # Loops through all proteins in dataframe, pairing every protein with every other protein
        for second_element_index in range(first_element_index, len(dataframe)):
            second_element = {
                dataframe.loc[second_element_index, 'id']: dataframe.loc[second_element_index, 'sequence']}
            # Combines the first protein key/value pair with the second protein key/value pair
            both_elements = dict(first_element, **second_element)
            count += 1
            # Utilizes the write_fasta function to write the two proteins into one FASTA file
            write_fasta(both_elements, dimers=True)
    print('Fasta files generated: ' + str(count))


def first_with_all(dataframe):
    '''
    Generates FASTA files for the first protein in the intial fasta against every other protein
    :param dataframe: dataframe containing id and sequence information
    :return: outputs fasta
    '''
    count = 0
    # Saves the first protein in the df as the first element
    first_element = {dataframe.loc[0, 'id']: dataframe.loc[first_element_index, 'sequence']}
    # Loops through all other proteins in dataframe, pairing the first with every other
    for second_element_index in range(1, len(dataframe)):
        second_element = {
            dataframe.loc[second_element_index, 'id']: dataframe.loc[second_element_index, 'sequence']}
        # Combines the first protein key/value pair with the second protein key/value pair
        both_elements = dict(first_element, **second_element)
        count += 1
        # Utilizes the write_fasta function to write the two proteins into one FASTA file
        write_fasta(both_elements, dimers=True)
    print('Fasta files generated: ' + str(count))


def generate_fasta(run_type, home_path, data_path, fasta_initial_path, fasta_result_path):
    '''

    :param run_type: determines how the proteins are combined into files
    :param home_path: str of home path
    :param data_path: str of path to data folder specific for complex
    :param fasta_initial_path: str of path where file.fasta is saved
    :param fasta_result_path: str of path for dir where fasta files are output
    :return:
    '''
    # Load fasta file
    fasta_file = open(fasta_initial_path + '\\' + 'file.fasta')

    # Parse fasta file and load contents into df
    df = parse_fasta(fasta_file, data_path=data_path)

    # Changes to dir for saving files
    os.chdir(fasta_result_path)

    # Logic to determine how the proteins are combined to create FASTA files
    if run_type == 'all':
        # Generates all pairs of proteins
        all_pairs(df)
    if run_type == '1_with_all'
    # Changes back to home directory
    os.chdir(home_path)
