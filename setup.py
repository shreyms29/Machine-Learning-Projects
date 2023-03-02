from setuptools import setup,find_packages
from typing import List


PROJECT_NAME="shipment-pricing"
VERSION="0.0.1"
AUTHOR="Shreyas M S"
DESRCIPTION="Predicting the Shipment pricing"
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,    
packages=find_packages(),
install_requires=get_requirements_list()

)

