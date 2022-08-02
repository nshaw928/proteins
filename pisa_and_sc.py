import os
import pandas as pd

pisa_path = 'C:\\Users\\nshaw\\CCP4-8\\8.0\\bin\\pisa.exe'

def run_pisa(pdbfile):
    '''
    :param pdbfile: a pdb file containing two chains
    :return: a dataframe with the protein interface information
    '''
    file_name = pdbfile.split('.')[0] + '_pisa.xml'
    # Run pisa and save xml
    os.system(pisa_path + ' name -analyse ' + pdbfile)
    os.system('pisa name -xml interfaces >' + file_name)
    os.system('pisa name -erase')
    print(file_name)




def run_sc():
    pass
    # First line


run_pisa(pdbfile='C:\\Users\\nshaw\\OneDrive\\Desktop\\0.pdb')
