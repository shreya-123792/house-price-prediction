import streamlit as st
import pandas as pd
import joblib

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------
st.set_page_config(
    page_title="Real Estate Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------
st.markdown("""
<style>

.stApp{
    background:#F5F7FA;
}

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Hero Banner */
.hero{
background:
linear-gradient(rgba(15,76,129,0.75),
rgba(30,136,229,0.75)),
url("https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1600");

background-size:cover;
background-position:center;

padding:45px;
border-radius:20px;

box-shadow:0px 10px 30px rgba(0,0,0,0.2);

margin-bottom:25px;

color:white;
text-align:center;
}
            col1,col2,col3,col4 = st.columns(4)

col1.metric("📊 Dataset","21,613 Houses")

col2.metric("🤖 Algorithm","XGBoost")

col3.metric("📌 Features","20")

col4.metric("⚡ Deployment","Streamlit")

/* Cards */
.card{
    background:#FFFFFF;
    border-radius:18px;
    height:180px;
    padding:20px;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    box-shadow:0 8px 20px rgba(0,0,0,0.12);

    transition:0.3s;
}

.card:hover{
    transform:translateY(-6px);
    box-shadow:0 12px 28px rgba(0,0,0,0.18);
}

.card h2{
    color:#0F4C81;
    font-size:28px;
    font-weight:700;
    margin:10px 0;
    text-align:center;
}

.card p{
    font-size:18px;
    color:#555;
    font-weight:600;
    text-align:center;
}
/* Sidebar */
section[data-testid="stSidebar"]{
background:#0F4C81;
}

section[data-testid="stSidebar"] *{
color:white;
}

/* Button */
.stButton>button{
background:#0F4C81;
color:white;
border:none;
border-radius:10px;
padding:12px;
font-size:18px;
font-weight:bold;
width:100%;
}

.stButton>button:hover{
background:#1565C0;
}

/* Metric */
div[data-testid="metric-container"]{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# HERO SECTION
# -----------------------------------------------------
st.markdown("""
<div class='hero'>

<h1 style="
font-size:44px;
font-weight:700;
letter-spacing:0.5px;
margin-bottom:8px;">
🏠 Real Estate Price Prediction
</h1>

<p style="
font-size:19px;
font-weight:400;
color:#F2F2F2;">
AI-Powered Property Valuation using XGBoost Machine Learning
</p>

</div>
""", unsafe_allow_html=True)
model = joblib.load("models/house_price_model.pkl")

# -----------------------------------------------------
# PROFESSIONAL SIDEBAR
# -----------------------------------------------------
with st.sidebar:

    st.image(
        "https://img.icons8.com/color/240/home.png",
        width=120
    )

    st.markdown("## 🏠 Real Estate Price Prediction")

    st.markdown("---")

    st.markdown("""
### 📌 Project Overview

This web application predicts **residential property prices**
using an optimized **XGBoost Machine Learning model**.

The prediction is based on various house features such as:

- 🛏 Bedrooms
- 🛁 Bathrooms
- 📐 Living Area
- 🌍 Latitude & Longitude
- ⭐ Grade
- 🏞 Waterfront
- 📍 Location Score

---
""")

    st.markdown("### 🛠 Technologies")

    st.success("✔ Python")
    st.success("✔ Pandas")
    st.success("✔ NumPy")
    st.success("✔ Scikit-learn")
    st.success("✔ XGBoost")
    st.success("✔ Joblib")
    st.success("✔ Streamlit")

    st.markdown("---")

    
# DASHBOARD CARDS
# -----------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4, gap="large")

with c1:
    with st.container(border=True):
        st.markdown("## 🤖")
        st.markdown("### Model")
        st.write("XGBoost")

with c2:
    with st.container(border=True):
        st.markdown("## 📊")
        st.markdown("### Dataset")
        st.write("King Country House")

with c3:
    with st.container(border=True):
        st.markdown("## 📌")
        st.markdown("### Features")
        st.write("20 Features")

with c4:
    with st.container(border=True):
        st.markdown("## 💻")
        st.markdown("### Platform")
        st.write("Streamlit")

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("🏡 Property Information")
st.caption("Enter the property details below to predict the estimated house price.")
# ==========================================
# PROPERTY INPUT FORM
# ==========================================

import datetime

with st.expander("🏠 Property Details", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        house_id = st.number_input("House ID", value=1)

        bedrooms = st.number_input(
            "Bedrooms",
            min_value=1,
            max_value=10,
            value=3
        )

        bathrooms = st.number_input(
            "Bathrooms",
            min_value=1.0,
            max_value=10.0,
            value=2.0,
            step=0.5,
            format="%.1f"
        )

    with col2:

        floors = st.number_input(
            "Floors",
            min_value=1.0,
            max_value=5.0,
            value=1.0,
            step=0.5,
            format="%.1f"
        )

        sqft_living = st.number_input(
            "Living Area (sqft)",
            500,
            10000,
            1800
        )

        sqft_lot = st.number_input(
            "Lot Area (sqft)",
            500,
            50000,
            5000
        )

# ======================================
# Building Information
# ======================================

with st.expander("🏗 Building Information"):

    col1, col2 = st.columns(2)

    with col1:

        grade = st.selectbox(
            "Grade",
            list(range(1, 14)),
            index=6
        )

        condition = st.selectbox(
            "Condition",
            [1, 2, 3, 4, 5],
            index=2
        )

        view = st.selectbox(
            "View",
            [0, 1, 2, 3, 4]
        )

    with col2:

        waterfront = st.selectbox(
            "Waterfront",
            ["No", "Yes"]
        )

        waterfront = 1 if waterfront == "Yes" else 0

        yr_built = st.number_input(
            "Year Built",
            1900,
            2025,
            2000
        )

        yr_renovated = st.selectbox(
            "Year Renovated",
            [0] + list(range(1900, 2026))
        )
        # ==========================================
# LOCATION INFORMATION
# ==========================================

with st.expander("📍 Location Information", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        zipcode = st.number_input(
            "📮 Zipcode",
            min_value=98000,
            max_value=98200,
            value=98001
        )

        lat = st.number_input(
            "🌍 Latitude",
            value=47.5112,
            format="%.5f"
        )

        long = st.number_input(
            "🧭 Longitude",
            value=-122.257,
            format="%.5f"
        )

    with col2:

        sqft_above = st.number_input(
            "🏠 Sqft Above Ground",
            min_value=0,
            value=1180
        )

        sqft_basement = st.number_input(
            "🏗 Sqft Basement",
            min_value=0,
            value=0
        )

        sqft_living15 = st.number_input(
            "🏡 Nearby Living Area",
            min_value=0,
            value=1340
        )

        sqft_lot15 = st.number_input(
    "🌳 Nearby Lot Area",
    min_value=0,
    value=5650
)

location_score = st.slider(
    "📍 Location Score",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button("🔍 Predict House Price")

if predict:

    input_data = pd.DataFrame({

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

    prediction = model.predict(input_data)[0]

    usd_to_inr = 95.28
    prediction_inr = prediction * usd_to_inr

    st.success("✅ Prediction Generated Successfully!")

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#0F4C81,#1E88E5);
        padding:30px;
        border-radius:18px;
        color:white;
        text-align:center;
        box-shadow:0px 8px 20px rgba(0,0,0,0.2);
        ">

        <h3>💵 Estimated Price (USD)</h3>

        <h1>${prediction:,.2f}</h1>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#009688,#26A69A);
        padding:30px;
        border-radius:18px;
        color:white;
        text-align:center;
        box-shadow:0px 8px 20px rgba(0,0,0,0.2);
        ">

        <h3>🇮🇳 Estimated Price (INR)</h3>

        <h1>₹{prediction_inr:,.0f}</h1>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("🏡 Property Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Bedrooms",
            "Bathrooms",
            "Living Area",
            "Lot Area",
            "Grade",
            "Condition",
            "Zipcode"
        ],
        "Value": [
            bedrooms,
            bathrooms,
            sqft_living,
            sqft_lot,
            grade,
            condition,
            zipcode
        ]
    })

    st.dataframe(summary, use_container_width=True)
   