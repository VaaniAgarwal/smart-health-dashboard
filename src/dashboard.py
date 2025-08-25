import streamlit as st

PRIMARY_COLOUR = "#42AdAD"
BG_COLOUR = "#F9FAFB"
CARD_COLOUR = "white"
st.set_page_config(
    page_title="Smart Health Risk Prediction Dashboard",
    page_icon="🩺",
    layout="wide"
)

st.sidebar.title("🩺 Health Dashboard")
menu = st.sidebar.radio(
    "Choose a section:",
    ["Home", "Kidney Disease", "Liver Disease", "Heart Disease"]
)

if menu == "Home":
    st.markdown(
        f"""
        <div style="background-color:{CARD_COLOUR}; padding:2rem; border-radius:1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align:center;">
            <h1 style="color:{PRIMARY_COLOUR};">Smart Health Risk Prediction</h1>
            <p style="font-size:18px; color:#333;">A modern, user-friendly dashboard to assess health risks using advanced ML models.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

elif menu == "Kidney Disease":
    st.subheader("🧪 Kidney Disease Risk Form")
    with st.form("kidney_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age",min_value=1,max_value=100,step=1)
            bp = st.number_input("Blood Pressure",min_value=50,max_value=200,step=1)
        with col2:
            sugar = st.number_input("Blood Sugar",min_value=50,max_value=400,step=1)
            hemoglobin = st.number_input("Hemoglobin Level",min_value=3,max_value=18,step=1)
        submit_kidney = st.form_submit_button("🔍 Predict Risk")
        if submit_kidney:
            st.success("Placeholder: Kidney Disease Prediction Result will appear here.")

elif menu == "Liver Disease":
    st.subheader("🧬 Liver Disease Risk Form")
    with st.form("liver_form"):
        col1, col2 = st.columns(2)
        with col1:
            bilirubin = st.number_input("Bilirubin Level",min_value=0.1,max_value=10.0,step=0.1)
            enzymes = st.number_input("Enzyme Count",min_value=10,max_value=2000,step=10)
        with col2:
            protein = st.number_input("Protein Level",min_value=2.0,max_value=9.0,step=0.1)
            albumin = st.number_input("Albumin Level",min_value=1.0,max_value=6.0,step=0.1)
        submit_liver = st.form_submit_button("🔍 Predict Risk")
        if submit_liver:
            st.success("Placeholder: Liver Disease Prediction Result will appear here.")

elif menu == "Heart Disease":
    st.subheader("❤️ Heart Disease Risk Form")
    with st.form("heart_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age",min_value=1,max_value=100,step=1)
            chol = st.number_input("Cholesterol",min_value=100,max_value=400,step=1)
        with col2:
            bp = st.number_input("Resting Blood Pressure",min_value=80,max_value=200,step=1)
            max_hr = st.number_input("Max Heart Rate",min_value=60,max_value=220,step=1)
        submit_heart = st.form_submit_button("🔍 Predict Risk")
        if submit_heart:
            st.success("Placeholder: Heart Disease Prediction Result will appear here.")