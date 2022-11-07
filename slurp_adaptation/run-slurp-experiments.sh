#!/bin/bash

### Environment Variables
GPU_ID=0
export TOKENIZERS_PARALLELISM=false
export PYTHONPATH=`pwd`

### Hyperparameters
TASK=absa
TRAIN_BATCH_SIZE=24
EVAL_BATCH_SIZE=24
EPOCHS=10
SEED=212

# this is all domains, remove according to wish
# DOMAINS=recommendation,iot,cooking,datetime,transport,lists,takeaway,play,calendar,weather,general,qa,alarm,audio,social,email,music,news
SRC_DOMAINS=iot,cooking,datetime,transport,lists,takeaway,play,calendar,weather,general,qa,alarm,audio,social,email,music,news
TRG_DOMAIN=recommendation

# echo "Extracting DRFs for the current experiment."
# python /home/gurnoor/PADA/slurp_adaptation/drf_extraction.py \
# --domains ${SRC_DOMAINS} \
# --drf_set_location /home/gurnoor/PADA/slurp_adaptation/drf_sets

# echo "Annotating training examples with DRF-based prompts."
# python /home/gurnoor/PADA/slurp_adaptation/prompt_annotation.py \
# --domains ${SRC_DOMAINS} \
# --root_data_dir /home/gurnoor/PADA/slurp_adaptation/data \
# --drf_set_location /home/gurnoor/PADA/slurp_adaptation/drf_sets \
# --prompts_data_dir /home/gurnoor/PADA/slurp_adaptation/prompt_annotations

CUDA_VISIBLE_DEVICES=${GPU_ID} python /home/gurnoor/PADA/slurp_adaptation/train.py \
--dataset_name ${TASK} \
--src_domains ${SRC_DOMAINS} \
--trg_domain ${TRG_DOMAIN} \
--num_train_epochs ${EPOCHS} \
--train_batch_size ${TRAIN_BATCH_SIZE} \
--eval_batch_size ${EVAL_BATCH_SIZE} \
--seed ${SEED}

