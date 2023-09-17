# import logging 
# from sklearn.pipeline import Pipeline
# from pipelines_for_ml.preprocessing.flight_data.flight_data_complete_preprocessing import create_preprocessing_pipeline

# # Configure the logging settings
# logging.basicConfig(level=logging.ERROR) 
# logger = logging.getLogger(__name__)

# def load_preprocessing_pipeline():
#     try:
#         # Add a print statement to check the file path
#         print("Loading preprocessing pipeline from:")
#         # print("Classes",ColumnNameFixer,CalculateFlightDistance,CustomFlightDataFeaturesAdder,DropColumns,LabelEncoderTransformer)
#         # Load the preprocessing pipeline from the joblib file
#         preprocess_pipeline = create_preprocessing_pipeline()
#         return preprocess_pipeline
#     except Exception as e:
#         # Log the error message if an exception is raised
#         logging.error(f"Error in create_preprocessing_pipeline: {str(e)}")
#         logger.error(f"Error in create_preprocessing_pipeline: {str(e)}")
#         raise