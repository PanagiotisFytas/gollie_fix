#!/bin/bash
#SBATCH --job-name=GoLLIE-7B_CodeLLaMA_biotriplex
#SBATCH --gres=gpu:1
#SBATCH --output=.slurm/GoLLIE-7B_CodeLLaMA_biotriplex.out.txt
#SBATCH --error=.slurm/GoLLIE-7B_CodeLLaMA_biotriplex.err.txt


conda activate gollie310

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=pfytas-ltl
export WANDB_PROJECT=GoLLIE_biotriplex

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

export PYTHONPATH="$PYTHONPATH:$PWD"
CONFIGS_FOLDER="configs/model_configs"


# Call this script from root directory as: sbatch bash_scripts/GoLLIE-7B_CodeLLaMA_train_full_model.sh


torchrun --standalone --master_port 37223 --nproc_per_node=2 src/run.py  ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_train_biotriplex.yaml