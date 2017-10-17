import pickle
import csv
import numpy as np
from sklearn.model_selection import GridSearchCV

def save_obj(obj, name):
    print("Saving given object to file {}".format(name))
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    print("Loading object {}".format(name))
    with open(name, 'rb') as f:
        return pickle.load(f)

# Something is wrong with the function below -- messed header; don't use it for
# now
def GridCV_scores_to_csv(gs_clf, export_file):
    with open(export_file, 'w') as outfile:
        csvwriter = csv.writer(outfile, delimiter=',')

    # Create the header using the parameter names
        header = ["mean","std"]
        param_names = [param for param in gs_clf.param_grid]
        header.extend(param_names)

        csvwriter.writerow(header)

        for config in gs_clf.cv_results_:
            # Get mean and standard deviation
            mean = config[1]
            std = np.std(config[2])
            row = [mean,std]

            # Get the list of parameter settings and add to row
            params = [str(p) for p in config[0].values()]
            row.extend(params)
            csvwriter.writerow(row)
