import xgboost as xgb
import argparse
import sys
import os
from saving_loading import *

#####################################
p = {
    "max_depth":int(5.0),
    "eta":0.06,
    "gamma":0.0,
    "num_boost_round":int(100.0),
    "early_stopping_rounds":int(10.0)
}
#####################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run CV for xgboost with particular combination of parameters')
    parser.add_argument("X",
                        help = "path to CSR matrix with features of pairs (theorem, premise)")
    parser.add_argument("y",
                        help = "path to CSV file with labels reflecting relevances of pairs (theorem, premise)")
    parser.add_argument("output_directory",
                        help = "path to directory where performance of tested model should be saved")
    args = parser.parse_args()

    y = read_csv(os.path.abspath(args.y), type_of_records = "int")
    X = load_obj(os.path.abspath(args.X))
    output_directory = os.path.abspath(args.output_directory)

    dtrain = xgb.DMatrix(X, label = y)
    params = {
        "max_depth":p["max_depth"],
        "eta":p["eta"],
        "gamma":p["gamma"],
        "objective":"binary:logistic"
    }
    x = xgb.cv(
        params = params,
        dtrain = dtrain,
        num_boost_round = p["num_boost_round"],
        early_stopping_rounds = p["early_stopping_rounds"],
        nfold = 4,
        metrics = {"error","auc","logloss"}
    )

    output_name = os.path.join(output_directory, "_".join(map(str, list(p.values())))+".pkl")
    save_obj({"params":p, "stats":x}, output_name)

