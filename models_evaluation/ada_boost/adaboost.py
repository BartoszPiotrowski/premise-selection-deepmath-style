from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import sys
import os
from tools import *

data = load_obj(sys.argv[1])
y = data["labels"]
X = data["features"]

clf = AdaBoostClassifier(n_estimators=1000)

scores = cross_val_score(clf, X, y, cv=4)
save_obj(scores, "adaboost_scores.pkl")
