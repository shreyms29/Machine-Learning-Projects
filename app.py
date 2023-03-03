from flask import Flask
import os,sys
from shipment.logger import logging
from shipment.exception import ShipmentExpection

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("we are testing")
    except Exception as e:
        shipment = ShipmentExpection(e,sys)
        logging.info(shipment.error_message)
        logging.info("we are testing logging")
    return "CI CD pipeline has been established"

if __name__=="__main__":
    app.run(debug=True)

    