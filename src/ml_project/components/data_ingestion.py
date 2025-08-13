import pandas as pd
from src.ml_project.logging.logger import logger
import sys
import os 
from pathlib import Path
import zipfile
from src.ml_project.utils.common import get_size
import urllib.request as request
from src.ml_project.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_path):
            filename,headers = request.urlretrieve(url = self.config.SOURCE_URL,filename = self.config.local_data_path)
            logger.info(f"{filename} downloaded successfully")
        else:
            logger.info("file already exist")
    
    def extract_data(self):
        unzip_data = self.config.unzip_path
        os.makedirs(unzip_data,exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_path,'r') as f:
            f.extractall(unzip_data)


    
