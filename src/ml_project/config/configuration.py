from pathlib import Path
import os
import sys
from src.ml_project.constant import *
from src.ml_project.logging.logger import logger
from src.ml_project.utils.common import read_yaml,create_dir
from src.ml_project.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self,config_file_path = CONFIG_FILE_PATH,schema_file_path = SCHEMA_FILE_PATH,params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_dir([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_dir([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            SOURCE_URL = config.SOURCE_URL,
            local_data_path = config.local_data_path,
            unzip_path = config.unzip_path

        )

        return data_ingestion_config