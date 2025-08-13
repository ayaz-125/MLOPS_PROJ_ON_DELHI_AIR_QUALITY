from src.ml_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.ml_project.logging.logger import logger


STAGE_NAME = "DATA INGESTION STAGE"

try:
        print("xxxxxxxxxxx==========xxxxxxxxxx")
        logger.info(F"<<<<<<<<<<<<<<   {STAGE_NAME} --STARTED>>>>>>>>>>>>>>>>>>>>>")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(F"<<<<<<<<<<<<<<<<<<<<   {STAGE_NAME}  -- COMPLETED>>>>>>>>>>>>>>>")
        print("xxxxxxxxxxx==========xxxxxxxxxx")

except Exception as e:
        raise e