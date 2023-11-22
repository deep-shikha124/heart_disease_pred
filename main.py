from flask import Flask, request
from utils.validateRequest import validateRequest
from utils.model import Model

app = Flask(__name__)

@app.route("/predict",methods=["POST"])
@validateRequest()
def predict():
  model : Model

  model = Model(request.json)
  return {"predicted_output" : int(model.predict())}

if __name__ == "__main__":
  app.run(debug=True)