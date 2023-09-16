from fastapi import APIRouter, HTTPException
from schemas.flight_info import FlightInfo
from utils.preprocessing.pipeline_1.preprocessing_pipeline import load_preprocessing_pipeline
from utils.preprocessing.pipeline_1.custom_transformer_classes import ColumnNameFixer, CalculateDistance, CustomFeaturesAdder, DropColumns, LabelEncoderTransformer

router = APIRouter()

@router.post('/preprocessdata')
async def preprocess_data(input_data: FlightInfo):
    try:
        preprocessing_pipeline = load_preprocessing_pipeline()
        # preprocessed_data = preprocessing_pipeline.transform(input_data)
        return {"preprocessed": input_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
