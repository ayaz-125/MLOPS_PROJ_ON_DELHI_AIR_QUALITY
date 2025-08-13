from pathlib import Path
from typing import Any
import os
import logging
import sys
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from src.ml_project.logging.logger import logger
import json
import joblib


@ensure_annotations
def read_yaml(path_do_yaml_file_ka:Path) -> ConfigBox:
    with open(path_do_yaml_file_ka) as file:
        content = yaml.safe_load(file)
        return ConfigBox(content)


@ensure_annotations
def create_dir(directory_name:list,verbose=True):
    for path in directory_name:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info("Directory created successfully")

@ensure_annotations
def save_json(path_location_jaha_save_krna_hai:Path,data:dict):
    with open(path_location_jaha_save_krna_hai,'w') as f:
        json.dump(f,data,indent=4)

@ensure_annotations
def load_json(path_jaha_pr_alredy_json_file_hai:Path) ->ConfigBox:
    with open(path_jaha_pr_alredy_json_file_hai) as file:
        content = json.load(file)
        return ConfigBox(content)
    
@ensure_annotations
def save_bin(path_jaha_par_save_krna_hai:Path,data:object):
    joblib.dump(value=data,filename=path_jaha_par_save_krna_hai)

@ensure_annotations
def load_bin(path_jaha_se_load_krega:Path) ->object:
    data = joblib.load(path_jaha_se_load_krega)
    return data

@ensure_annotations
def get_size(path_jiska_size_janna_hai:Path) ->str:
    size_in_kb = round(os.path.getsize(path_jiska_size_janna_hai)/1024)
    return f"~{size_in_kb} KB"        