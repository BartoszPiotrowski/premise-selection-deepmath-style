import argparse
import sys
import os
import numpy as np
sys.path.append('../../..')
from tools.saving_loading import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Collect scores originating from grid search')
    parser.add_argument("scores_dir", help = "path to directory containing scores")
    parser.add_argument("filename", nargs='?', default="None", help = "filename for saving scores")
    args = parser.parse_args()
    scores_files = listdir_fullpath(os.path.abspath(args.scores_dir))
    filename = os.path.normpath(args.filename)
    param_scores = [load_obj(f) for f in scores_files]
    parameters = [list(i["params"].values()) + [len(i["stats"])] for i in param_scores]
    n_iters = [len(i["stats"]) for i in param_scores]
    scores = [i["stats"].tail(1).values.tolist()[0] for i in param_scores]
    parameters_names = list(param_scores[0]["params"].keys()).append("n_iters")
    scores_names = list(param_scores[0]["stats"])
    lll = list(zip(parameters, scores))
    ll = [i[0] + i[1] for i in lll]
    if filename == "None":
        printll(ll)
    else:
        save_csv(ll, filename)
