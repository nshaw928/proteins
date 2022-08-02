import os

pisa_path =

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
    print()



def run_sc():
    # First line
