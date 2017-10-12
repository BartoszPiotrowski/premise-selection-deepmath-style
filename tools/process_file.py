import hashlib
import os
import csv
import sys
from saving_loading import *


if __name__ == "__main__":
    try:
        features_of_theorems = load_obj(sys.argv[1])
        hashes_of_features = load_obj(sys.argv[2])
        with open(sys.argv[4],"r") as f:
            list_of_lines = f.read().splitlines()
    except:
        print("Call 'python3 process_file.py features_of_theorems.pkl hashes_of_features.pkl target_directory filename'")
        sys.exit(0)

    labels = []
    features = []
    for i in list_of_lines:
        i = i.split(" ")
        if (i[0] == "C"):
            theorem_features = features_of_theorems[i[1]]
            hashes_of_theorem_features = [hashes_of_features[i] for i in theorem_features]
        else:
            premise_features = features_of_theorems[i[1]]
            hashes_of_premise_features = [hashes_of_features[i] for i in premise_features]
            features.append(["T_" + i for i in hashes_of_theorem_features] +
                            ["P_" + i for i in hashes_of_premise_features])
            if (i[0] == "+"): labels.append(1)
            if (i[0] == "-"): labels.append(0)

    save_obj({"labels":labels, "features":features},
             os.path.join(sys.argv[3], os.path.basename(sys.argv[4]) + ".pkl"))
