"""
Module to view prompt annotations for a given domain
:author: gurnoorsingh (20221115)
"""
import os
import torch
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--domain', '-d', help='Domain name')
args = parser.parse_args()

PROMPTS_DIR = "/home/gurnoor/PADA/slurp_adaptation/prompt_annotations"
PROMPT_FILENAME = "annotated_prompts_train.pt"
DATA_DIR = "/home/gurnoor/PADA/slurp_adaptation/data"

with open(os.path.join(DATA_DIR, args.domain, "train"), 'rb') as fh:
    data = pickle.load(fh)

with open(os.path.join(PROMPTS_DIR, args.domain, PROMPT_FILENAME), 'rb') as fh:
    annotations = torch.load(fh)
    assert len(data[0]) == len(data[1]) == len(annotations)
    for i in range(len(annotations)):
        print(' '.join(data[0][i]))
        print(data[1][i])
        print(annotations[i])