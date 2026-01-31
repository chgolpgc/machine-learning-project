from pathlib import Path
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
