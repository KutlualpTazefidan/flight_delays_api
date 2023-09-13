# utils/model_loader.py
import joblib
import sklearn
from config import settings

def load_model(model_path):
    loaded_model = joblib.load(model_path)
    if not isinstance(loaded_model, sklearn.base.BaseEstimator):
        raise ValueError("The loaded object is not a scikit-learn model.")
    return loaded_model