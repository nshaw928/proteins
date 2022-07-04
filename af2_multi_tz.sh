#!/bin/bash
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -c 6
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu_requeue
#SBATCH --error=af2_multi_tz.err
#SBATCH --output=af2_multi_tz.out
#SBATCH -t 0-23:00:00
#SBATCH --mem=40G
#SBATCH --requeue

alphafold.py --fasta_paths=/n/scratch3/users/n/nis806/tz_full_data/$1 --max_template_date=2020-05-14 --db_preset=full_dbs --output_dir=/n/scratch3/users/n/nis806/tz_full_results/ --data_dir=/n/shared_db/alphafold/ --model_preset=multimer --run_relax --num_multimer_predictions_per_model=1