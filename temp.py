# import pickle

# with open("/home/gurnoor/PADA/data/absa_data/device/train", 'rb') as f:
#     a = pickle.load(f)
#     print(a[0][0], a[1][0])
import jsonlines

s = set()
with jsonlines.open("/home/gurnoor/massive/1.0/data/en-US.jsonl") as fh:
    for row in fh: s.add(row["scenario"])

print(','.join(s))