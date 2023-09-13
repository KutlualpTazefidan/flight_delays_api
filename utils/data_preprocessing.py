import joblib

# Load your pre-processing pipeline
pipeline = joblib.load('your_pipeline.joblib')

def preprocess_data(input_data):
    preprocessed_data = pipeline.transform(input_data)
    return preprocessed_data