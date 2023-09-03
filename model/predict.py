import joblib

model = joblib.load('model/model.pkl')

def predict(input_data):
    return model.predict(input_data)
