import xgboost as xgb
import argparse
import sys
sys.path.append("../../..")
from tools.saving_loading import *
from tools.inspecting import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take xgboost model and tell me importance of features')
    parser.add_argument("model",
                        help = "file containing model (saved by xgboost method)")
    parser.add_argument("list_of_features",
                       help = "ordered list of feature names saved in csv file")
    parser.add_argument("filename",
                       help = "name of file where to save important features")
    parser.add_argument("importance_type", choices=['weight','gain'],
                       nargs='?', default="weight",
                       help = "importance type from xgboost model")
    args = parser.parse_args()

    model = xgb.Booster()
    model.load_model(os.path.normpath(args.model))
    list_of_features = read_csv(os.path.normpath(args.list_of_features),
                                delimiter = ";")
    filename = os.path.normpath(args.filename)
    importance_type = args.importance_type

    imp = model.get_score(importance_type=importance_type)
    imp = [(int(k.replace("f", "")), imp[k]) for k in sorted(imp, key=imp.get, reverse=True)]
    l = len(list_of_features)
    g = lambda i: "thm" if i[0] < l else "prm"
    imp_names = [(i[0], g(i), list_of_features[i[0]%l], i[1]) for i in imp]
    header = [("f_number", "thm_prm", "feature", "importance")]
    save_csv(header + imp_names, filename, delimiter = ";")
