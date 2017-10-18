import argparse
import sys
import os
sys.path.append('../../..')
from tools.job_generator import generate_jobs

print("Name:", __name__)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate set of jobs from a given template')
    parser.add_argument("template",
                        help = "path to template")
    parser.add_argument("grid",
                        help = "path to txt file specifying grid of parameters")
    parser.add_argument("output_directory",
                        help = "path to direcory for saving scripts with jobs")
    args = parser.parse_args()

    template = os.path.abspath(args.template)
    grid = os.path.abspath(args.grid)
    output_directory = os.path.abspath(args.output_directory)

generate_jobs(template, grid, output_directory)
