import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Titanic Survival Demo", page_icon="🚢", layout="centered")
st.title("Titanic Survival Prediction")
st.caption("Educational demonstration only — not a real-world decision tool.")

@st.cache_resource
def load_model():
    return joblib.load("titanic_model.joblib")

try:
    model = load_model()
except Exception:
    st.error("Model file not found. Run the notebook and save titanic_model.joblib in this folder.")
    st.stop()

st.subheader("Passenger details")
pclass = st.selectbox("Passenger class", [1, 2, 3], index=2)
sex = st.selectbox("Sex", ["female", "male"])
age = st.slider("Age", 0, 80, 29)
sibsp = st.number_input("Siblings / spouse aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents / children aboard", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0, step=1.0)
embarked = st.selectbox("Port of embarkation", ["S", "C", "Q"])
title = st.selectbox("Title", ["Mr", "Mrs", "Miss", "Master", "Other"])
deck = st.selectbox("Cabin deck", ["Unknown", "A", "B", "C", "D", "E", "F", "G", "T"])
ticket_prefix = st.selectbox("Ticket prefix", ["NUMERIC_OR_OTHER", "PC", "CA", "A", "SOTON", "STON", "W", "Other"])

family_size = int(sibsp + parch + 1)
is_alone = int(family_size == 1)

if st.button("Predict", type="primary"):
    passenger = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex,
        "Age": float(age),
        "SibSp": int(sibsp),
        "Parch": int(parch),
        "Fare": float(fare),
        "Embarked": embarked,
        "Title": title,
        "FamilySize": family_size,
        "IsAlone": is_alone,
        "Deck": deck,
        "TicketPrefix": ticket_prefix
    }])
    try:
        prediction = int(model.predict(passenger)[0])
        probability = float(model.predict_proba(passenger)[0, 1])
        st.metric("Estimated survival probability", f"{probability:.1%}")
        if prediction == 1:
            st.success("Model prediction: Survived")
        else:
            st.info("Model prediction: Did not survive")
        st.caption("This prediction is based on a small historical dataset and should not be interpreted as a reliable real-world prediction.")
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
        st.write("Check that the notebook's saved model and app.py are from the same project version.")
