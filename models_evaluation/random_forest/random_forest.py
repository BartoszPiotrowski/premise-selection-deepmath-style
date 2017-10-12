from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import sys
import os
from tools import *

data = load_obj(sys.argv[1])
y = data["labels"]
X = data["features"]

clf = RandomForestClassifier(n_estimators=1000, n_jobs = 12)

scores = cross_val_score(clf, X, y, cv=5)
save_obj(scores, "random_forest_scores.pkl")
