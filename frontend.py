import streamlit as st
import requests

# API URL
API_URL = "http://localhost:8000/predict"

# App Title and Intro
st.set_page_config(page_title="Credit Default Detector", layout="centered")
st.title("💳 Credit Default Detector")
st.markdown("Use this tool to predict whether a customer is likely to **default on credit**.")

st.markdown("---")
st.subheader("📋 Customer Profile")

with st.form("credit_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        marriage = st.selectbox("👰 Marital Status", options=['single', 'married', 'others'])
        education = st.selectbox("🎓 Education Level", options=['university', 'high school', 'graduate school', 'others'])
        sex = st.selectbox("⚧ Gender", options=['male', 'female'])
        limit_bal = st.number_input("💰 Credit Limit", min_value=0.0, step=1000.0)

    with col2:
        pay_0 = st.selectbox("📅 Pay Status: Current Month", options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_2 = st.selectbox("📅 Pay Status: 2 Months Ago", options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_3 = st.selectbox("📅 Pay Status: 3 Months Ago", options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_4 = st.selectbox("📅 Pay Status: 4 Months Ago", options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_5 = st.selectbox("📅 Pay Status: 5 Months Ago", options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_6 = st.selectbox("📅 Pay Status: 6 Months Ago", options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

    with col3:
        bill_amt1 = st.number_input("🧾 Bill Amount Last Month", min_value=0.0)
        bill_amt2 = st.number_input("🧾 Bill 2 Months Ago", min_value=0.0)
        bill_amt3 = st.number_input("🧾 Bill 3 Months Ago", min_value=0.0)
        bill_amt4 = st.number_input("🧾 Bill 4 Months Ago", min_value=0.0)
        bill_amt5 = st.number_input("🧾 Bill 5 Months Ago", min_value=0.0)
        bill_amt6 = st.number_input("🧾 Bill 6 Months Ago", min_value=0.0)

    st.subheader("💵 Payments Made")
    col4, col5, col6 = st.columns(3)

    with col4:
        pay_amt1 = st.number_input("Paid Last Month", min_value=0.0)
    with col5:
        pay_amt2 = st.number_input("Paid 2 Months Ago", min_value=0.0)
    with col6:
        pay_amt3 = st.number_input("Paid 3 Months Ago", min_value=0.0)

    col7, col8, col9 = st.columns(3)

    with col7:
        pay_amt4 = st.number_input("Paid 4 Months Ago", min_value=0.0)
    with col8:
        pay_amt5 = st.number_input("Paid 5 Months Ago", min_value=0.0)
    with col9:
        pay_amt6 = st.number_input("Paid 6 Months Ago", min_value=0.0)

    submit = st.form_submit_button("🔍 Predict")

    if submit:
        input_data = {
            'marriage': marriage,
            'sex': sex,
            'education': education,
            'LIMIT_BAL': limit_bal,
            'pay_0': pay_0,
            'pay_2': pay_2,
            'pay_3': pay_3,
            'pay_4': pay_4,
            'pay_5': pay_5,
            'pay_6': pay_6,
            'Bill_amt_1': bill_amt1,
            'Bill_amt_2': bill_amt2,
            'Bill_amt_3': bill_amt3,
            'Bill_amt_4': bill_amt4,
            'Bill_amt_5': bill_amt5,
            'Bill_amt_6': bill_amt6,
            'pay_amt1': pay_amt1,
            'pay_amt2': pay_amt2,
            'pay_amt3': pay_amt3,
            'pay_amt4': pay_amt4,
            'pay_amt5': pay_amt5,
            'pay_amt6': pay_amt6
        }

        try:
            response = requests.post(API_URL, json=input_data)
            if response.status_code == 200:
                result = response.json()
                st.success(f"🎯 **Prediction Result:** `{result['response']}`")
            else:
                st.error(f"❌ API error ({response.status_code}): {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"🚫 Could not connect to the API server.\n\nError: `{e}`")


