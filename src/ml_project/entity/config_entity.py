from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    SOURCE_URL:str
    local_data_path:Path
    unzip_path:Path