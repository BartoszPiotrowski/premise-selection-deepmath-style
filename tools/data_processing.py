import hashlib
import csv
import numpy as np
import scipy.sparse as sps
import os.path
from .saving_loading import *


def generate_hashes(features, output_dir):
    print("Reading features from", features)

    with open(features, "r") as f:
        list_of_lines = f.read().splitlines()
    theorem_names = []
    features_of_theorems = []
    for i in list_of_lines:
        i = i.split(":")
        theorem_names.append(i[0])
        features_of_theorems.append(i[1].replace('"', '').split(", "))

    features_of_theorems_dict = dict(zip(theorem_names, features_of_theorems))

    print("Number of theorems: ", len(features_of_theorems))

    counter = 0
    for i in features_of_theorems:
        counter += len(i)
    print("Average number of features per theorem:", counter/len(theorem_names))

    set_of_features = set().union(*features_of_theorems)
    print("Number of different features:", len(set_of_features))

    list_of_features = list(set_of_features)
    hashes_of_features = {x : hashlib.md5(x.encode('utf-8')).hexdigest()
                                 for x in list_of_features}

#TODO use your function
    with open(os.path.join(output_dir, "hashes_of_features.csv"), 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter =";",quoting=csv.QUOTE_MINIMAL)
        for feature, hash_key in hashes_of_features.items():
           writer.writerow([hash_key, feature])
    print("Hashes saved to hashes_of_features.csv")

    save_obj(hashes_of_features,
             os.path.join(output_dir, "hashes_of_features.pkl"))
    save_obj(features_of_theorems_dict,
             os.path.join(output_dir, "features_of_theorems.pkl"))

def concatenate_coos_to_csr(input_directory, output_directory):
    list_of_files = [input_directory + "/" + i for i in os.listdir(input_directory)]
    print("Reading", len(list_of_files), "files from", input_directory, "directory")

    list_of_labels = []
    list_of_coo_matrices = []
    for file in list_of_files:
        f = load_obj(file)
        list_of_labels.extend(f["labels"])
        coo_matrix = f["coo_matrix"]
        list_of_coo_matrices.append(coo_matrix)
    print("Concatenating", len(list_of_coo_matrices), "matrices into csr matrix")
    csr_matrix = sps.vstack(list_of_coo_matrices, format="csr")
    assert len(list_of_labels) == csr_matrix.shape[0]
    save_obj(list_of_labels, os.path.join(output_directory, "labels.pkl"))
    save_csv(list_of_labels, os.path.join(output_directory, "labels.csv"))
    save_obj(csr_matrix, os.path.join(output_directory, "features_csr.pkl"))
