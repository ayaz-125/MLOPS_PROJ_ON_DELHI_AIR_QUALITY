from pathlib import Path
import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "ml_project"

list_of_project = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training.py",
    f"src/{project_name}/pipeline/prediction.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/prediction.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/__init__.py",
    "research/__init__.py",
    "params.yaml",
    "schema.yaml",
    "config/config.yaml",
    "main.py",
    "app.py",
    "DOCKERFILE",
    "test.py",
    "requirements.txt",
    "setup.py",

]

for filepath in list_of_project:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info("file directory created successfully")
    if not os.path.exists(filepath) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:  # this line is very important because it helps to make the files inside the folder 
            pass
    else:
        logging.info("file is already available")



    