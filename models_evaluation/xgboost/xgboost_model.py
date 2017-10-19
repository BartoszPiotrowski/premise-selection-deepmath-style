import xgboost as xgb
import sys
sys.path.append("../..")
from tools.saving_loading import *

y = read_csv(sys.argv[1], type_of_records = "int")
X = load_obj(sys.argv[2])
dtrain = xgb.DMatrix(X, label = y)
param = {
    "max_depth":10,
    "eta":0.06,
    "objective":"binary:logistic"
}
num_round = 2000
model = xgb.train(param, dtrain, num_round)
model.save_model("xgboost_2000.model")

