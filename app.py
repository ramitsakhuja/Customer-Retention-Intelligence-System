import streamlit as st
import pandas as pd
import joblib

model = joblib.load("xgb_churn_model.pkl")

feature_columns = joblib.load("feature_columns.pkl")
st.title("Customer Retention Intelligence System")
st.write("Predict customer churn and generate retention insights.")

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    max_value=72,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Credit card (automatic)",
        "Bank transfer (automatic)",
        "Mailed check"
    ]
)

if st.button("Predict Churn Risk"):

    input_df = pd.DataFrame(columns=feature_columns)
    input_df.loc[0] = 0

    input_df["tenure"] = tenure
    input_df["MonthlyCharges"] = monthly_charges

    if contract == "One year":
        input_df["Contract_One year"] = 1

    elif contract == "Two year":
        input_df["Contract_Two year"] = 1

    if internet_service == "Fiber optic":
        input_df["InternetService_Fiber optic"] = 1

    elif internet_service == "No":
        input_df["InternetService_No"] = 1

    if payment_method == "Credit card (automatic)":
        input_df[
            "PaymentMethod_Credit card (automatic)"
        ] = 1

    elif payment_method == "Electronic check":
        input_df[
            "PaymentMethod_Electronic check"
        ] = 1

    elif payment_method == "Mailed check":
        input_df[
            "PaymentMethod_Mailed check"
        ] = 1

    prediction = model.predict(input_df)[0]

    st.subheader("Prediction Result")
    if prediction == 1:
        st.error("High Churn Risk")
    else:
        st.success("Low Churn Risk")
    probability = model.predict_proba(input_df)[0][1]
    st.write(f"Churn Probability: {probability:.2%}")