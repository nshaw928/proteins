import pandas as pd
import os
import shutil
import json


def generate_pdbs_from_af(fasta_result_path, alphafold_result_path, piscore_data_path, data_path, pdb_for_dropbox):

    # Create DataFrame using test data set to check for AlphaFold success or which ones need run again
    df = pd.DataFrame({'protA_protB': [], 'protA': [], 'protB': [], 'rank': [], 'pLDDT': []})

    # Populate protA_protB, protA, and protB from the fasta files
    for file in os.listdir(fasta_result_path):
        # Save strings to be used in the df
        protA_protB = file.split('.')[0]
        protA = protA_protB.split('_')[0]
        protB = protA_protB.split('_')[1]
        # Create dict with prot names and add to df
        temp_dict = {'protA_protB': protA_protB, 'protA': protA, 'protB': protB}
        temp_df = pd.DataFrame([temp_dict])
        df = pd.concat([df, temp_df], ignore_index=True)

    # Saved ranked pdbs in new folder with name protA_protB_#.pdb (created earlier)

    for folder in os.listdir(alphafold_result_path):
        if os.path.exists(alphafold_result_path + '\\' + folder + '\\ranked_0.pdb'):
            # Saves copy for renaming to index
            shutil.copyfile(alphafold_result_path + '\\' + folder + '\\ranked_0.pdb',
                            piscore_data_path + '\\ranked_0.pdb')
            new_file_name = '\\' + folder + '.pdb'
            os.rename(piscore_data_path + '\\ranked_0.pdb', piscore_data_path + new_file_name)
            # Saves copy for uploading to dropbox
            shutil.copyfile(alphafold_result_path + '\\' + folder + '\\ranked_0.pdb',
                            pdb_for_dropbox + '\\ranked_0.pdb')
            new_file_name = '\\' + folder + '.pdb'
            os.rename(piscore_data_path + '\\ranked_0.pdb', piscore_data_path + new_file_name)
        else:
            pass

    # Update df with rankings for each protein set and their pLDDT score
    # Updates df with rank 0 for proteins that have completed the AlphaFold run
    for file in os.listdir(piscore_data_path):
        temp_both_prots = file.split('.')[0]
        for index in df.index:
            if df.loc[index, 'protA_protB'] == temp_both_prots:
                df.loc[index, 'rank'] = '0'
            else:
                pass

    # Renames files to index value in df
    for file in os.listdir(piscore_data_path):
        for index in df.index:
            if file.split('.')[0] == df.loc[index, 'protA_protB']:
                os.rename(piscore_data_path + '\\' + file, piscore_data_path + '\\' + str(index) + '.pdb')

    # Parse ranking_debug.json for PLDDT scores and add to df
    for index in df.index:
        if df.loc[index, 'rank'] == '0':
            with open(alphafold_result_path + '\\' + df.loc[index, 'protA_protB']
                      + '\\' + 'ranking_debug.json') as ranking_json:
                ranking_data = json.load(ranking_json)
                ranking_data = list(ranking_data.values())[0]
                ranks = []
                ranks.append(list(ranking_data.values())[0:5])
                ranks = ranks[0]
                ranks.sort(reverse=True)
                for index2 in df.index:
                    if df.loc[index2, 'rank'] == '0' and (df.loc[index2, 'protA_protB'] == df.loc[index, 'protA_protB']):
                        df.loc[index2, 'pLDDT'] = ranks[0]
                    else:
                        pass
    print(df)

    # Save df as csv to be used later
    df.to_csv(data_path + '\\pre_piscore.csv')