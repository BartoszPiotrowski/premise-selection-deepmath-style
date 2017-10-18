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

def printll(ll):
    for l in ll:
        print(" ".join(map(str, l)))

