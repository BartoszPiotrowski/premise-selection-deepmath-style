import xgboost as xgb
import sys
import os
import csv
import pandas as pd
from sklearn.model_selection import GridSearchCV
from tools import *

if __name__ == "__main__":
    try:
        data = load_obj(sys.argv[1])
        outcome_name = sys.argv[2]
    except:
        print('Call "python3 xgboost_grid_search.py csr_matrix.pkl outcome_name"')
        sys.exit(0)

y = data["labels"]
X = data["features"]

dtrain = xgb.DMatrix(X, label = y)

grid_params = {'max_depth': [5, 10],
             'learning_rate': [0.1, 0.2, 0.3]}
const_params = {'n_estimators': 5}
grid = GridSearchCV(xgb.XGBClassifier(**const_params), grid_params,
                             scoring = 'accuracy', cv = 5, n_jobs = 2)
g = grid.fit(X, y)
save_obj(g, outcome_name)
