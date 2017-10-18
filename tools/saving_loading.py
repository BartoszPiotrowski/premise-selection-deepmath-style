import pickle
import os
import csv
import numpy as np
import itertools
from sklearn.model_selection import GridSearchCV

def save_obj(obj, filename):
    print("Saving given object to file {}".format(filename))
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(filename):
    print("Loading object {}".format(filename))
    with open(filename, 'rb') as f:
        return pickle.load(f)

def save_csv(obj, filename, delimiter = ","):
    print("Saving given object to CSV file {}".format(filename))
    if isinstance(obj, np.ndarray):
        np.savetxt(filename, obj, delimiter=delimiter)
    elif isinstance(obj, list):
        with open(filename, "w") as file:
            writer = csv.writer(file, delimiter=delimiter, quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
            if not isinstance(obj[0], list):
                obj = [[i] for i in obj]
            writer.writerows(obj)
    else:
        print("Cannot save object of this type as csv file.")

# to be tested more
def read_csv(filename, delimiter = ",", type_of_records = "string"):
    print("Reading CSV file {}".format(filename))
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar='"')
        if type_of_records == "int":
            data = [list(map(int, row)) for row in reader]
        elif type_of_records == "float":
            data = [list(map(float, row)) for row in reader]
        else:
            data = [list(row) for row in reader]
        if len(data[0]) == 1:
            data = list(itertools.chain.from_iterable(data))
        return data


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

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
