"""
Module to get drf sets for a given domain
:author: gurnoorsingh (20221115)
"""
import os
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--domain', '-d', help='Domain for which to get drfs')
args = parser.parse_args()

DRFS_DIR = "/home/gurnoor/PADA/slurp_adaptation/drf_sets"
with open(os.path.join(DRFS_DIR, args.domain + ".pkl"), 'rb') as fh:
    drf_set = pickle.load(fh)
    print(drf_set)
