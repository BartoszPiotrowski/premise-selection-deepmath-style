from sklearn.ensemble.forest import ExtraTreesClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import sys
import os
from tools import *

data = load_obj(sys.argv[1])
y = data["labels"]
X = data["features"]

clf = ExtraTreesClassifier(n_estimators=1000, n_jobs = -1)

scores = cross_val_score(clf, X, y, cv=5)
save_obj(scores, "extra_trees_scores.pkl")
