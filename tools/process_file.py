import numpy as np
import scipy.sparse as sps
import os
import sys
from saving_loading import *


if __name__ == "__main__":
    try:
        dict_of_features = load_obj(sys.argv[1])
        set_of_features = read_csv(sys.argv[2], delimiter = ";")
        output_direcory = sys.argv[3]
        file_name = sys.argv[4]
    except:
        print("Call 'python3 process_file.py dict_of_features.pkl set_of_features.csv output_directory file_name'")
        sys.exit(0)

    with open(file_name,"r") as f:
        list_of_lines = f.read().splitlines()

    def bin_vector(set_of_all_features, features):
        return [i in features for i in set_of_all_features]

    first_line = list_of_lines[0].split(" ")
    assert first_line[0] == "C"
    theorem_features = dict_of_features[first_line[1]]
    theorem_features_bin_vec = bin_vector(set_of_features, theorem_features)
    labels = []
    bin_vectors = []
    for i in range(1, len(list_of_lines)):
        l = list_of_lines[i].split(" ")
        premise_features = dict_of_features[l[1]]
        premise_features_bin_vec = bin_vector(set_of_features, premise_features)
        bin_vectors.append(theorem_features_bin_vec + premise_features_bin_vec)
        if (l[0] == "+"): labels.append(1)
        if (l[0] == "-"): labels.append(0)

    assert len(bin_vectors) == len(labels)
    assert len(labels) == len(list_of_lines) - 1

    coo_matrix = sps.coo_matrix(np.array(bin_vectors))

    assert coo_matrix.shape[0] == len(labels)
    assert coo_matrix.shape[1] == len(set_of_features) * 2

    save_obj({"labels":labels, "coo_matrix":coo_matrix},
             os.path.join(output_direcory, os.path.basename(file_name) + ".pkl"))
