import sys
import os.path
import argparse
import shlex
import subprocess
from tools.data_processing import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Prepare data for ML experiments')
    parser.add_argument("input_directory",
                        help = "path to directory containing files with information about relevances of premises for proving theorems")
    parser.add_argument("features",
                        help = "path to file containing features of theorems")
    parser.add_argument("output_directory",
                        help = "path to direcory for saving processed data")
    parser.add_argument("n_jobs",
                       help = "number of cores to use for the task of preparing data",
                        type = int, default=4)
    args = parser.parse_args()

    input_directory = os.path.normpath(args.input_directory)
    features = os.path.normpath(args.features)
    output_directory = os.path.normpath(args.output_directory)
    n_jobs = args.n_jobs

    make_dict_and_set_of_features(features, output_directory)

    subprocess.call(["mkdir", os.path.join(output_directory, "coo")])
    l1 = subprocess.Popen(['find', input_directory, "-type", "f"], stdout=subprocess.PIPE)
    l2 = subprocess.Popen(['parallel', '-j' + str(n_jobs), 'python3',
                           os.path.join("tools", 'process_file.py'),
                           os.path.join(output_directory, 'dict_of_features.pkl'),
                           os.path.join(output_directory, 'set_of_features.csv'),
                           os.path.join(output_directory, 'coo'), '{}'],
                           stdin=l1.stdout, stdout=subprocess.PIPE)
    l1.stdout.close()
    out, err = l2.communicate()

    concatenate_coos_to_csr(os.path.join(output_directory, "coo"),
                            output_directory)
