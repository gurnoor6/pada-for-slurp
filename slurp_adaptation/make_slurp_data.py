"""
Script to make slurp dataset into the required format
to be used by PADA scripts
The required format is a pickled file containing list of sentences
and labels
:author: gurnoorsingh (20221108)
"""
import os
import re
import jsonlines
import pickle
from collections import defaultdict

DATA_FILE = "/home/gurnoor/massive/1.0/data/en-US.jsonl"

def annotate(utt, annot_utt):
    length = len(utt.split())
    labels = ['O'] * length
    for slot_filler in re.findall("\[(.*?)\]", annot_utt):
        slot, filler = slot_filler.split(":")[0].strip(), slot_filler.split(":")[1].strip()
        start = 0
        for idx, filler_item in enumerate(filler.split()):
            if idx == 0:
                labels[utt.split().index(filler_item)] = 'B'
                start = utt.split().index(filler_item)
            else:
                labels[utt.split().index(filler_item, start)] = 'I'
    
    return labels


domains = set()
with jsonlines.open(DATA_FILE) as fh:
    for row in fh:
        domains.add(row["scenario"])

for domain in domains:
    dir_path = f"/home/gurnoor/PADA/slurp_adaptation/data/{domain}"
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

for domain in domains:
    sentences, labels = defaultdict(lambda: []), defaultdict(lambda: [])
    with jsonlines.open(DATA_FILE) as fh:
        for row in fh:
            if row["scenario"] != domain:
                continue
        
            sentences[row["partition"]].append(row["utt"].split())
            labels[row["partition"]].append(annotate(row["utt"], row["annot_utt"]))
    
    dir_path = f"/home/gurnoor/PADA/slurp_adaptation/data/{domain}"
    modes = ["train", "test", "dev"]
    for mode in modes:
        with open(f"{dir_path}/{mode}", 'wb') as fh:
            pickle.dump((sentences[mode], labels[mode]), fh)

    


