from string import Template
from itertools import product
import pandas as pd
import sys
import os

grid = {
    "max_depth":[5, 10],
    "eta":[0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3],
    "gamma":[0, 0.1],
    "num_boost_round":[10, 100, 200],
    "early_stopping_rounds":[10]
}
comb = pd.DataFrame(list(product(*list(grid.values()))))
template_name = sys.argv[1]
jobs_directory = sys.argv[2]
template = Template(open(template_name).read())
for i in range(comb.shape[0]):
    d = dict(zip(grid.keys(), comb.loc[i,:]))
    print(d)
    job = template.substitute(d)
    job_file_name = os.path.join(jobs_directory,
                    "_".join(map(str, list(d.values())))+".job.py")
    with open(job_file_name, "w") as txt:
        txt.write(job)
