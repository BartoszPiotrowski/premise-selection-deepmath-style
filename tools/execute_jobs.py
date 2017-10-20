import sys
import os.path
import argparse
import shlex
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Execute python jobs from a given repository')
    parser.add_argument("jobs",
                        help = "path to a directory containing python jobs to execute")
    parser.add_argument("X",
                        help = "path to file with feature matrix")
    parser.add_argument("y",
                        help = "path to file with labels")
    parser.add_argument("outcomes",
                        help = "path to a directory for collecting outcomes")
    parser.add_argument("n_cores",
                       help = "number of cores to use for the execution of jobs",
                        type = int, nargs='?', default=4)
    args = parser.parse_args()

    jobs = os.path.normpath(args.jobs)
    X = os.path.normpath(args.X)
    y = os.path.normpath(args.y)
    outcomes = os.path.normpath(args.outcomes)
    n_cores = args.n_cores

    subprocess.call(["mkdir", os.path.join(outcomes)])
    l1 = subprocess.Popen(['find', jobs, "-name", "*job.py"], stdout=subprocess.PIPE)
    l2 = subprocess.Popen(['parallel', '-j' + str(n_cores),
                           'python3', '{}', X, y, outcomes],
                           stdin=l1.stdout, stdout=subprocess.PIPE)
    l1.stdout.close()
    out, err = l2.communicate()

