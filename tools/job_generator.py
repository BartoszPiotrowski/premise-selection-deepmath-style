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

    g = {}
    for l in list_of_lines:
        param, numbers_str = l.split(":")
        numbers = [int_float(i) for i in numbers_str.split(", ")]
        g[param] = numbers
    comb = list(product(*list(g.values())))
    template = Template(open(template).read())
    for i in comb:
        d = dict(zip(g.keys(), i))
        job = template.substitute(d)
        job_file_name = os.path.join(output_directory,
                        "_".join(map(str, list(d.values())))+".job.py")
        with open(job_file_name, "w") as txt:
            txt.write(job)
