import os
import pickle
import torch

# DIR = "/home/gurnoor/PADA/slurp_adaptation/drf_sets"
# l = list()
# for file in os.listdir(DIR):
#     with open(os.path.join(DIR, file), 'rb') as f:
#         a = pickle.load(f)
#         l.append(set(a))

# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if len(l[i].intersection(l[j])):
#             print(l[i])
#             print(l[j])
#             print(l[i].intersection(l[j]))

x = torch.load("/home/gurnoor/PADA/slurp_adaptation/prompt_annotations/social/annotated_prompts_train.pt")
for a in x: 
    if len(a) != 5: print(a)

# import jsonlines

# s = set()
# with jsonlines.open("/home/gurnoor/massive/1.0/data/en-US.jsonl") as fh:
#     for row in fh: s.add(row["scenario"])

# print(','.join(s))