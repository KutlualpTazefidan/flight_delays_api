"""
flight_data_preprocessing Module

This module defines a set of custom data preprocessing transformers and a preprocessing pipeline
for preparing flight data for machine learning tasks.

Transformers:
- ColumnNameFixer: Fixes column names by replacing spaces and hyphens with underscores.
- CalculateFlightDistance: Calculates the distance between two geographical coordinates.
- CustomFlightDataFeaturesAdder: Adds custom features to the data, such as time-based features.
- DropColumns: Drops specified columns from the dataset.
- LabelEncoderTransformer: Performs label encoding on specified categorical columns.

Preprocessing Pipeline:
- The preprocessing pipeline applies the above transformers in a specific order to prepare the data
  for machine learning.

Usage:
- Import the transformers and the preprocessing pipeline from this module for data preparation.
- Create an instance of the preprocessing pipeline and fit/transform your data.

For more details, refer to the individual docstrings within each transformer class.
"""
import joblib
import logging
from sklearn.pipeline import Pipeline
from .deserialize import (deserialize_calculate_flight_distance,
                         deserialize_add_additional_flight_data_features,
                         deserialize_fix_column_names,
                         deserialize_drop_columns,
                         deserialize_label_encoder_transformer)

# Configure the logging settings
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Modify this function to include deserialization logic for custom classes
def create_preprocessing_pipeline():
    try:
        # Load serialized custom transformers
        serialized_pckg_path = "pipelines_for_ml/preprocessing/flight_data/serialized_data/"
        loaded_fix_column_names = deserialize_fix_column_names(serialized_pckg_path+'column_name_fixer.pkl')
        loaded_calculate_flight_distance = deserialize_calculate_flight_distance(serialized_pckg_path+'calculate_flight_distance.pkl')
        loaded_add_additional_flight_data_features = deserialize_add_additional_flight_data_features(serialized_pckg_path+'add_additional_flight_data_features.pkl')
        loaded_label_encoder_transformer = deserialize_label_encoder_transformer(serialized_pckg_path+'label_encoder_transformer.pkl')
        loaded_drop_columns = deserialize_drop_columns(serialized_pckg_path+'drop_columns.pkl')

        # Create the preprocessing pipeline
        preprocessing_pipeline = Pipeline([
            ('column_name_fixer', loaded_fix_column_names),
            ('calculate_flight_distance', loaded_calculate_flight_distance),
            ('add_additional_flight_data_features', loaded_add_additional_flight_data_features),
            ('drop_columns', loaded_drop_columns),
            ('encode_labels', loaded_label_encoder_transformer)
        ])

        return preprocessing_pipeline
    except Exception as e:
        # Log the error message if an exception is raised
        logging.error(f"Error in create_preprocessing_pipeline: {str(e)}")
        logger.error(f"Error in create_preprocessing_pipeline: {str(e)}")
        raise