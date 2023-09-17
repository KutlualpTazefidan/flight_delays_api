import joblib
from sklearn.preprocessing import LabelEncoder
from pipelines_for_ml.preprocessing.classes.flight_data_transformers import(CalculateFlightDistance, 
                                                                            AddAdditionalFlightDataFeatures)
from pipelines_for_ml.preprocessing.classes.transformers import(FixColumnNames, 
                                                                DropColumns, 
                                                                LabelEncoderTransformer)

# Deserialization for ColumnNameFixer
def deserialize_fix_column_names(filename):
    state = joblib.load(filename)
    transformer = FixColumnNames()
    return transformer

# Deserialization for CalculateDistance
def deserialize_calculate_flight_distance(filename):
    state = joblib.load(filename)
    transformer = CalculateFlightDistance()
    return transformer

# Deserialization for CustomFeaturesAdder
def deserialize_add_additional_flight_data_features(filename):
    state = joblib.load(filename)
    transformer = AddAdditionalFlightDataFeatures()
    return transformer

# Deserialization for DropColumns
def deserialize_drop_columns(filename):
    state = joblib.load(filename)
    transformer = DropColumns(state['columns_to_drop'])
    return transformer

# Deserialization for LabelEncoderTransformer
def deserialize_label_encoder_transformer(filename):
    state = joblib.load(filename)
    transformer = LabelEncoderTransformer(columns=state['columns'])
    transformer.label_encoders = {col: LabelEncoder() for col in state['columns']}
    
    for col, classes in state['label_encoders'].items():
        label_encoder = transformer.label_encoders[col]
        label_encoder.classes_ = classes
    
    return transformer