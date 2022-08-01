import pandas as pd
import os

def extract_piscore(data_path, piscore_result_path):

    # Load df from CSV
    df = pd.read_csv(data_path + '\\pre_piscore.csv')
    # Rename first column to 'index' for matching later
    df.rename(columns={'Unnamed: 0': 'index'}, inplace=True)
    # Save number of columns in df
    columns_df = df.shape[1]

    # Loop through folders to extract the data for PIS
    for folder in os.listdir(piscore_result_path):
        # The folder name in the output is the index of the data frame where it needs to be saved
        pair_index = int(folder.split('_')[0])
        for item in os.listdir(piscore_result_path + '\\' + folder):
            # This is the directory where our results are
            if item == 'pi_output':
                pis_path = piscore_result_path + '\\' + folder + '\\' + 'pi_output'
                # We need two files from this directory, the features and PIS
                for data in os.listdir(pis_path):
                    # Get features csv and add to df
                    if data.split('_')[0] == 'filter':
                        df_features = pd.read_csv(pis_path + '\\' + data)
                        df_features.rename(columns={'pdb': 'index'}, inplace=True)
                        # Adds features to df the first time
                        if df.shape[1] == columns_df or df.shape[1] == (columns_df + 3):
                            df = df.merge(df_features, on='index', how='outer')
                        # Adds features to df every other time, doing this through assignment
                        if df_features.shape[0] == 1:
                            df.loc[pair_index, 'Num_intf_residues'] = df_features.loc[0, 'Num_intf_residues']
                            df.loc[pair_index, 'Polar'] = df_features.loc[0, 'Polar']
                            df.loc[pair_index, 'Hydrophobhic'] = df_features.loc[0, 'Hydrophobhic']
                            df.loc[pair_index, 'Charged'] = df_features.loc[0, 'Charged']
                            df.loc[pair_index, 'contact_pairs'] = df_features.loc[0, 'contact_pairs']
                            df.loc[pair_index, ' sc'] = df_features.loc[0, ' sc']
                            df.loc[pair_index, ' hb'] = df_features.loc[0, ' hb']
                            df.loc[pair_index, ' sb'] = df_features.loc[0, ' sb']
                            df.loc[pair_index, ' int_solv_en'] = df_features.loc[0, ' int_solv_en']
                            df.loc[pair_index, ' int_area'] = df_features.loc[0, ' int_area']
                            df.loc[pair_index, ' pvalue'] = df_features.loc[0, ' pvalue']
                    else:
                        pass
                    # Get PIS csv and add to df
                    if data.split('_')[0] == 'pi':
                        df_pis = pd.read_csv(pis_path + '\\' + data)
                        df_pis.rename(columns={'#PDB': 'index'}, inplace=True)
                        # Adds PIS to the df the first time
                        if df.shape[1] == columns_df or df.shape[1] == (columns_df + 12):
                            df = df.merge(df_pis, on='index', how='outer')
                        # Adds PIS to df every other time
                        if df_pis.shape[0] == 1:
                            df.loc[pair_index, 'predicted_class'] = df_pis.loc[0, 'predicted_class']
                            df.loc[pair_index, 'pi_score'] = df_pis.loc[0, 'pi_score']
                    else:
                        pass
            else:
                pass

    # Save Dataframe for analysis
    df.to_csv(data_path + '\\pi_scores.csv')