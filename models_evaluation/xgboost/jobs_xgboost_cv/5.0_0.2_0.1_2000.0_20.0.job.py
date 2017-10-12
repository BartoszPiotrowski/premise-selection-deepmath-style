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
    "max_depth":int(5.0),
    "eta":0.2,
    "gamma":0.1,
    "num_boost_round":int(2000.0),
    "early_stopping_rounds":int(20.0)
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

