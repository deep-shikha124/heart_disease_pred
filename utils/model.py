import pickle
import numpy as np
from .constant import headers

class Model:
    model = pickle.load(open('final_model.sav','rb'))
    input_data_as_numpy_array = []

    def __init__(self,data):
       dataTuple = tuple(data[header] for header in headers)
       self.input_data_as_numpy_array = np.asarray(dataTuple).reshape(1,-1)

    def predict(self):
       return self.model.predict(self.input_data_as_numpy_array)[0]
