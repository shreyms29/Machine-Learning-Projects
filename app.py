from flask import Flask
from shipment.logger import logging

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    logging.info("we are tseting logging")
    return "CI CD pipeline has been established"

if __name__=="__main__":
    app.run(debug=True)

    