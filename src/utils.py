import os
from pathlib import Path
import pickle
import sys
from src.exception import CustomException

def find_project_root(marker: str="setup.py"):
    """
    Function to find the root project path based on a marker. 
    """
    current = Path(__file__).resolve()
    try:
        for parent in [current] + list(current.parents):
            if (parent / marker).exists():
                return parent
    except Exception as e:
        CustomException(e, sys )

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)