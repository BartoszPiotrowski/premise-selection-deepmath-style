# premise-selection-deepmath-style

Machine Learning experiments for premise selection for Mizar-originating data.
We are planning to beat neural nets from the [Deepmath paper](https://arxiv.org/abs/1606.04442) with help of modern fancy ML algorithms like xgboost, ExtraTrees, et al.
Probably some sophisticated techniques of data preprocessing and densification will help.

# Data preparation

Original data comes from https://github.com/JUrban/deepmath
More precisely, we take
* [these](https://github.com/JUrban/deepmath/tree/master/trivdata) files witch contain names of theorems along with balanced set of useful and uneuseful premises for proving them
* [this](https://github.com/JUrban/deepmath/blob/master/mizar40/features.gz) file providing description of every theorem (premise) by features

In order to train ML models on the data we preprocessed it to the following shape:
1. Every theorem (premise) was associated with a binary vector representing features possesed by it.
2. For every pair (theorem, premise) for which we have have information from the data about relevance of the premise for proving the theorem was labelled according to this information by 0 or 1, and linked to concatenation of two binary vectors associated to this pair.
3. We have 522528 such pairs and 451706 different features, thus resulting (very sparse) matrix has size 522528 x 903412.
4. The matrix is saved in Compressed Sparse Row format (and its size is 202M; in dense representation it took > 20G).

Original and preprocessed data are in ./data
* CSR matrix with features: ./data/features_csr.pkl
* labels: .data/labels.pkl and .data/labels.csv

You can reproduce data preprocessing by running
```
python3 prepare_data.py data/original_data/trivdata/ data/original_data/features data_output 4
```
where `data_output_dir` is directory for preprocessed data and number `4` at the end indicates number of cores you want to use to preprocess data.

