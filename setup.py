from setuptools import setup,find_packages
from typing import List


PROJECT_NAME="shipment-pricing"
VERSION="0.0.3"
AUTHOR="Shreyas M S"
DESRCIPTION="Predicting the Shipment pricing"
REQUIREMENTS_FILE_NAME="requirements.txt"



def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = [lib_name.replace("\n","") for lib_name in requirement_file.readlines()]
        print(requirement_list)
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")
        return requirement_list



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,    
packages=find_packages(),
install_requires=get_requirements_list()
)

