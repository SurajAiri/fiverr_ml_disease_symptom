import pickle
from symptoms import model_symptoms

class DiseaseDetector:
    __MODEL_PATH = 'models/v2/random_forest-v2.pkl'

    def __load_model(self, path):
        with open(path, 'rb') as f:
            model = pickle.load(f)
        return model

    def __parse_symptoms(self,symptoms):
        sym = []
        for s in model_symptoms:
            if s in symptoms:
                sym.append(1)
            else:
                sym.append(0)
        return sym
    
    def __init__(self):
        self.__model = self.__load_model(self.__MODEL_PATH)

    def predict(self,symptoms) -> str:
        syms = self.__parse_symptoms(symptoms)
        return self.__model.predict([syms])[0]
 