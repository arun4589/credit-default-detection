from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import MODELVERSION,predict_default,model
from schema.user_input import UserInput
from schema.model_output import PredictionResponse



app=FastAPI()

@app.get('/')
def home():
    return {
        'message':"This is an API for Credit card default detection"
    
    }

@app.get('/health')
def health_check():
    return{
        'status':'OK',
        'model version': MODELVERSION,
        'model_loaded':model is not None
    }

@app.post('/predict',response_model=PredictionResponse)
def prediction(user_input:UserInput):
    input_df = {
        'marriage':user_input.marriage_status,
        'sex':user_input.gender,
        'education':user_input.edu_status,
        'pay_0':user_input.pay_0,
        'pay_2':user_input.pay_2,
        'pay_3':user_input.pay_3,
        'pay_4':user_input.pay_4,
        'pay_5':user_input.pay_5,
        'pay_6':user_input.pay_6,
        'Bill_amt1':user_input.Bill_amt_1,
        'pay_amt1':user_input.pay_amt1,
        'pay_amt2':user_input.pay_amt2,
        'pay_amt3':user_input.pay_amt3,
        'AVG_Bill_amt':user_input.AVG_Bill_amt,
        'PAY_TO_BILL_ratio':user_input.PAY_TO_BILL_ratio,
        'avg_pay_amt':user_input.avg_pay_amt,
        'utilisation_ratio':user_input.utilization_ratio,
        'delay_count':user_input.delay_count
    }
    try:
        prediction = predict_default(input_df)
        
        return JSONResponse(status_code=200,content={"response": prediction})
    except Exception as e:
        return JSONResponse(status_code=200,content=str(e))
    

