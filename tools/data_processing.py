import csv
import numpy as np
import scipy.sparse as sps
import os.path
from .saving_loading import *


def make_dict_and_set_of_features(features_file, output_directory):

    features_file = os.path.abspath(features_file)
    stats = open(os.path.join(output_directory, "stats.txt"), 'w')
    stats.write("Reading features from {}\n".format(features_file))

    with open(features_file, "r") as f:
        list_of_lines = f.read().splitlines()

    dict_of_features = {}
    for i in list_of_lines:
        i = i.split(":")
        theorem_name = i[0]
        theorem_features = i[1].replace('"', '').split(", ")
        dict_of_features[theorem_name] = theorem_features

    assert len(list_of_lines) == len(dict_of_features)

    stats.write("Number of theorems: {}\n".format(len(dict_of_features)))

    lengths = [len(i) for i in dict_of_features.values()]
    save_csv(lengths, os.path.join(output_directory, "lengths.csv"))
    stats.write("Average number of features per theorem: {}\n".format(sum(lengths)/len(lengths)))
    stats.write("Minimal number of features per theorem: {}\n".format(min(lengths)))
    stats.write("Maximal number of features per theorem: {}\n".format(max(lengths)))

    set_of_features = set().union(*dict_of_features.values())
    stats.write("Number of different features: {}\n".format(len(set_of_features)))

    save_obj(dict_of_features, os.path.join(output_directory, "dict_of_features.pkl"))
    save_csv(list(set_of_features), os.path.join(output_directory, "set_of_features.csv"), delimiter = ":")
    stats.close()

def concatenate_coos_to_csr(input_directory, output_directory):
    list_of_files = [os.path.join(input_directory, "/", i) for i in os.listdir(input_directory)]
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
