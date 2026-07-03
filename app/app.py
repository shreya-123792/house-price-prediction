import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("models/house_price_model.pkl")

# Title
st.title("🏠 House Price Prediction")
st.write("Enter the house details below:")

# Input Fields
house_id = st.number_input("House ID", value=1)

bedrooms = st.number_input("Bedrooms", min_value=1, value=3)

bathrooms = st.number_input("Bathrooms", min_value=1.0, value=2.0)

sqft_living = st.number_input("Living Area (sqft)", value=2000)

sqft_lot = st.number_input("Lot Area (sqft)", value=5000)

floors = st.number_input("Floors", value=1.0)

waterfront = st.selectbox("Waterfront", [0, 1])

view = st.slider("View", 0, 4, 0)

condition = st.slider("Condition", 1, 5, 3)

grade = st.slider("Grade", 1, 13, 7)

sqft_above = st.number_input("Sqft Above", value=1500)

sqft_basement = st.number_input("Sqft Basement", value=500)

yr_built = st.number_input("Year Built", value=1990)

yr_renovated = st.number_input("Year Renovated (0 if never)", value=0)

zipcode = st.number_input("Zipcode", value=98001)

lat = st.number_input("Latitude", value=47.5)

long = st.number_input("Longitude", value=-122.2)

sqft_living15 = st.number_input("Nearby Living Area", value=2000)

sqft_lot15 = st.number_input("Nearby Lot Area", value=5000)

location_score = st.number_input("Location Score", value=0.5)

# Prediction
if st.button("Predict Price"):

    data = pd.DataFrame({
        "id": [house_id],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "sqft_living": [sqft_living],
        "sqft_lot": [sqft_lot],
        "floors": [floors],
        "waterfront": [waterfront],
        "view": [view],
        "condition": [condition],
        "grade": [grade],
        "sqft_above": [sqft_above],
        "sqft_basement": [sqft_basement],
        "yr_built": [yr_built],
        "yr_renovated": [yr_renovated],
        "zipcode": [zipcode],
        "lat": [lat],
        "long": [long],
        "sqft_living15": [sqft_living15],
        "sqft_lot15": [sqft_lot15],
        "location_score": [location_score]
    })

    # Predict the price
    prediction = model.predict(data)

    # Convert USD to INR
    usd_price = prediction[0]
    usd_to_inr = 95.28
    inr_price = usd_price * usd_to_inr

    # Show results
    st.success(f"🏡 Predicted House Price (USD): ${usd_price:,.2f}")
    st.success(f"🇮🇳 Predicted House Price (INR): ₹{inr_price:,.2f}")

    st.subheader("Entered Details")
    st.write(data)

    st.balloons()