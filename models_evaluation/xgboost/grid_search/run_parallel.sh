ls -1 models_evaluation/xgboost/grid_search/jobs/*.job.py | time parallel -j4 "python3 {} data/MPTP2078/features_csr.pkl data/MPTP2078/labels.csv models_evaluation/xgboost/grid_search/jobs_out"
