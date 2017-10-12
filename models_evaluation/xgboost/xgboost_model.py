import xgboost as xgb
from sklearn.model_selection import train_test_split
import sys
import os
import sklearn.metrics as sklm
from tools import *

data = load_obj(sys.argv[1])
y = data["labels"]
X = data["features"]
dtrain = xgb.DMatrix(X, label = y)
#####################################
p = {
    "max_depth":3,
    "eta":1,
    "gamma":0,
    "num_boost_round":4,
    "early_stopping_rounds":2
}
#####################################
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

output_name = os.path.join("output_of_jobs", "_".join(map(str, list(p.values())))+".pkl")
save_obj({"params":p, "stats":x}, output_name)

