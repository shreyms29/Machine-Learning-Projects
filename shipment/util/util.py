import yaml
from shipment.exception import ShipmentExpection
import os,sys

def read_yaml_file(file_path:str)->dict:
    
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise ShipmentExpection(e,sys) from e    