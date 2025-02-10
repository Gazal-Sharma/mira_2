import streamlit as st
from mira_sdk import MiraClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

st.title("Health Tracker with BMI Analysis")

weight = st.number_input("Enter your weight (kg):", min_value=1, max_value=300, value=70)
height = st.number_input("Enter your height (m):", min_value=1.0, max_value=3.0, value=1.75)  # Fixed float issue
activity_level = st.selectbox("Select your activity level:", ["Sedentary", "Light", "Moderate", "Heavy"])

if st.button("Analyze Health"):
    if weight and height and activity_level:
        input_data = {"weight": weight, "height": height, "activity_level": activity_level}
        response = client.flow.execute("tt1230344/healthtracker", input_data)
        st.write(response.get("result", "No response from Mira AI"))
    else:
        st.warning("Please fill in all fields.")
