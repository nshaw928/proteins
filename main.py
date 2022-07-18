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
    os.chdir(home_path)

# Set path variables
data_path = home_path + '\\data'
fasta_initial_path = data_path + '\\fasta_initial'
fasta_result_path = data_path + '\\fasta_result'
alphafold_result_path = data_path + '\\alphafold_result'
piscore_data_path = data_path + '\\piscore_data'
piscore_result_path = data_path + '\\piscore_result'

# Check datasets for stage of project


# Function creates all combinations of FASTA files from one
def generate_fastas():
    # This dictionary contains HGNC gene names (key) and uniprot id (value) pairs for easy referencing
    # This is manually defined, so I can ensure the HGNC names are correct, as they are not always represented on UNIPROT
    # In the future, automating this dictionary is something that is possible and would aid in easy use of the program
    uniprot_id_dict = {
        "TMEM107": "Q6UX40",
        "TMEM17": "Q86X19",
        "TMEM231": "Q9H6L2",
        "TMEM67": "Q5HYA8",
        "TMEM216": "Q9P0N5",
        "TMEM237": "Q96Q45",
        "TMEM218": "A2RU14",
        "TCTN1": "Q2MV58",
        "TCTN2": "Q96GX1",
        "TCTN3": "Q6NUS6",
        "B9D1": "Q9UPM9",
        "B9D2": "Q9BPU9",
        "MKS1": "Q9NXB0",
        "CC2D2A": "Q9P2K1",
        "AHI1": "Q8N157",
        "CEP290": "O15078",
        "IQCB1": "Q15051",
        "ATXN10": "Q9UBB4",
        "INVS": "Q9Y283",
        "NPHP3": "Q7Z494",
        "NEK8": "Q86SG6",
        "ANKS6": "Q68BC2",
        "ANKS3": "Q6ZW76",
        "NPHP1": "O15259",
        "RPGRIP1L": "Q68CZ1",
        "NPHP4": "O75161"
    }
    # I created the dict in the with swapped key and values so this just swaps them,
    # this is used later when adding the conventional names to the dataframe.
    # If, in the future, the above uniprot_id_dict is updated to ("UNIPROT_ID": "HGNC NAME" ...)
    # delete the following line of code.
    uniprot_id_dict = dict([(value, key) for key, value in uniprot_id_dict.items()])

    # Load fasta file

    fasta_file = open(fasta_initial_path + '\\' + 'file.fasta')

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

    # Create DataFrame with id, sequence, sequence_length, and name

    # Define the DataFrame that our sequence data will be stored in
    df = pd.DataFrame({'id': [], 'sequence': [], })
    df.head()

    # Fill DataFrame with our data
    for key, value in sequences_dict.items():
        temp_dict = {'id': key, 'sequence': value}
        df = df.append(temp_dict, ignore_index=True)

    # Adds sequence_length column
    df['sequence_length'] = df['sequence'].str.len()

    # Adds conventional names from the UniProt ID Dictionary I manually defined in the first block
    df['name'] = df['id'].map(uniprot_id_dict)

    # Function to write FASTA files


    # Define Function
    def write_fasta(data_dict, generate_dimers=False):
        """
        Takes a dictionary as input and outputs a FASTA formatted file.

        The function writes a FASTA formatted file using the keys as identifier lines, and the values as the sequences.
        Output file names are formatted as "key1_key2_key3_ect.fasta" and are deposited into the current directory.
        """

        # Sets file name and opens the file for modification
        file_name = []
        for key, value in data_dict.items():
            file_name.append(key)
            if generate_dimers and len(data_dict) == 1:
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
            if generate_dimers and len(data_dict) == 1:
                identifier_line = ">" + key + "\n"
                output_file.write(identifier_line)
                sequence_line = value + '\n'
                output_file.write(sequence_line)

        # Closes the file, ending editing
        output_file.close()

    # Function that splits DataFrame into all pairs

    # Define Function
    def generate_pairs_and_save_fastas(df, dimers=False):
        """
        Takes a dataframe as input and outputs a FASTA formatted files for every pair combination of proteins.

        The other argument taken by the function is dimers, which is set to false by default which will not allow the same
        protein to be printed twice in one FASTA file.
        However, if set to true one protein will be printed twice in one FASTA file, allowing AlphaFold to predict a
        potential dimer interface.

        The input dataframe must contain columns 'id' and 'sequence' for this code to work accurately without modification.
        This function is dependent on the write_fasta function written above.

        The functional also prints out how many files it creates.
        """
        count = 0
        # Loops through all proteins in dataframe
        for first_element_index in range(0, len(df)):
            first_element = {df.loc[first_element_index, 'id']: df.loc[first_element_index, 'sequence']}
            # Loops through all proteins in dataframe, pairing every protein with every other protein
            for second_element_index in range(first_element_index, len(df)):
                second_element = {df.loc[second_element_index, 'id']: df.loc[second_element_index, 'sequence']}
                # Combines the first protein key/value pair with the second protein key/value pair
                both_elements = dict(first_element, **second_element)
                count += 1
                # Utilizes the write_fasta function to write the two proteins into one FASTA file
                write_fasta(both_elements, generate_dimers=dimers)
        print(count)

    # Creates folder for results and changes to that folder
    os.chdir(fasta_result_path)

    # This block is simply for running the functions above
    generate_pairs_and_save_fastas(df, dimers=True)

    # Changes back to home directory
    os.chdir(home_path)

# Function creates pdb files for PI scoring and adds rank and PLDDT scores to df


# Function adds results of PI scoring to df
