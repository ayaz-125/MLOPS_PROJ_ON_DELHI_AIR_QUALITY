from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project.entity.config_entity import DataIngestionConfig
from src.ml_project.config.configuration import ConfigurationManager
from src.ml_project.logging.logger import logger


STAGE_NAME = "DATA INGESTION STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_data()


if __name__=="__main__":
    try:
        logger.info(F"<<<<<<<<<<<<<<{STAGE_NAME} --STARTED>>>>>>>>>>>>>>>>>>>>>")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(F"<<<<<<<<<<<<<<<<<<<<{STAGE_NAME}  -- COMPLETED>>>>>>>>>>>>>>>")
    except Exception as e:
        raise e