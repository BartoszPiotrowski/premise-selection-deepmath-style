import numpy as np
import scipy.sparse as sps
import sys
import os
from saving_loading import *


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        hashes_of_features = sys.argv[2]
        target_directory = sys.argv[3]
    except:
        print('Call "python3 filename hashes_of_features.pkl target_directory"')
        sys.exit(0)

    list_of_hashes = list(load_obj(hashes_of_features).values())
    list_of_features = ["T_" + i for i in list_of_hashes] + ["P_" + i for i in list_of_hashes]

    f = load_obj(filename)
    labels = f["labels"]
    features = f["features"]
    list_of_binary_vectors = []
    for f in features:
        binary_vector = [i in f for i in list_of_features]
        list_of_binary_vectors.append(binary_vector)
    coo_matrix = sps.coo_matrix(np.array(list_of_binary_vectors))
    save_obj({"labels":labels, "coo_matrix":coo_matrix}, os.path.join(target_directory, os.path.basename(filename)))
