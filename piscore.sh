#!/bin/bash
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -c 2
#SBATCH --partition=short
#SBATCH --error=piscore.err
#SBATCH --output=piscore.out
#SBATCH -t 0-1:00:00
#SBATCH --mem=5G

ccpem-python /nfs/sbgrid/programs/x86_64-linux/ccpem/1.6.0/lib/py2/ccpem/src/ccpem_core/tasks/atomic_model_validation/bfactor_analysis/analyse_bfactors.pyc /n/scratch3/users/n/nis806/piscore_result/