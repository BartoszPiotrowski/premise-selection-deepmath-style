from string import Template
from itertools import product
import sys
import os


def generate_jobs(template, grid, output_directory):
    with open(grid, encoding ='utf-8') as f:
        list_of_lines = f.read().splitlines()

    def int_float(s):
        f = float(s)
        i = int(f)
        return i if i == f else f

    params, numbers = [], []
    for l in list_of_lines:
        p, n = l.split(":")
        ns = [int_float(i) for i in n.split(", ")]
        params.append(p); numbers.append(ns)
    comb = list(product(*numbers))
    template = Template(open(template).read())
    for i in comb:
        d = dict(zip(params, i))
        job = template.substitute(d)
        job_file_name = os.path.join(output_directory,
                        "_".join(map(str, i))+".job.py")
        with open(job_file_name, "w") as txt:
            txt.write(job)
