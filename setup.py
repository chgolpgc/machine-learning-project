from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."    

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = [line.strip() for line in file.readlines()]
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="ml",
    version="0.1.0",
    author="Christopher Gonzalez",
    author_email="",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)