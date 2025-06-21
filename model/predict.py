import joblib
import pandas as pd



with open("model/random_forest_model.joblib",'rb') as f:
    model=joblib.load(f)


MODELVERSION='1.0.0'
classes= ['Not Default','Default']

def predict_default(input_df:dict):
    input=pd.DataFrame([input_df])
    prediction = model.predict(input)[0]
    probabilities = model.predict_proba(input)[0]
    confidence=max(probabilities)
    class_probs = dict(zip(classes,map(lambda p: round(p,4),probabilities)))
    return {
        'predicted_category':'Default' if int(prediction)==1 else 'Not Default',
        'confidence':round(confidence,4),
        'class_probabilities':class_probs
    }
