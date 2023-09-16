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

from sklearn.pipeline import Pipeline

from ..classes.transformers import (
    ColumnNameFixer,
    DropColumns, 
    LabelEncoderTransformer)

from ..classes.flight_data_transformers import (
    CalculateFlightDistance, 
    CustomFlightDataFeaturesAdder
    )

def create_preprocessing_pipeline():
    """
    Create and return a preprocessing pipeline.

    Returns:
        sklearn.pipeline.Pipeline: A preprocessing pipeline.
    """
    try:
        # Categorical features , label encoding is used
        categorical_columns = ['depstn', 'arrstn', 'status', 'arr_country', 'dep_country', 'season', 'airline_code', 'international_flight','ac','dep_iata','arr_iata','fltid']
        
        # Features to drop
        columns_to_drop = ['id', 'std', 'sta', 'fltid', 'arr_iata', 'dep_iata', 'ac']
        
        # Preprocessing steps in the pipeline
        preprocessing_steps = [
            ('column_name_fixer', ColumnNameFixer()),
            ('calculate_distance', CalculateFlightDistance()),
            ('custom_features_adder', CustomFlightDataFeaturesAdder()),
            ('label_encoding', LabelEncoderTransformer(categorical_columns)),
            ('drop_columns', DropColumns(columns_to_drop))

        ]

        # Create the pipeline
        preprocessing_pipeline = Pipeline(steps=preprocessing_steps)
        return preprocessing_pipeline
    except Exception as e:
        # Raise a custom exception with an informative message
        raise Exception(f"Error in create_preprocessing_pipeline: {str(e)}")