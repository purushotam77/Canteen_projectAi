import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Canteen Predictor", layout="wide")

# ---------------- DARK MODE ----------------
dark_mode = st.toggle("🌙 Dark Mode")

if dark_mode:
    bg = "#0f172a"
    card = "#1e293b"
    text = "#f1f5f9"
    primary = "#3b82f6"
else:
    bg = "#f8fafc"
    card = "#ffffff"
    text = "#1e293b"
    primary = "#2563eb"

# ---------------- CSS ----------------
st.markdown(f"""
<style>
.stApp {{
    background-color: {bg};
    color: {text};
}}

.box {{
    background: {card};
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.08);
}}

.card {{
    background: {card};
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    transition: 0.3s;
}}

.card:hover {{
    transform: translateY(-5px);
}}

.stButton>button {{
    width: 100%;
    background: {primary};
    color: white;
    border-radius: 8px;
    height: 45px;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h2 style='text-align:center;'>Smart Canteen Queue Prediction</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Vaishali Food Park</p>", unsafe_allow_html=True)

# ---------------- MAIN BOX ----------------
st.markdown('<div class="box">', unsafe_allow_html=True)

# BASIC INPUT
col1, col2 = st.columns(2)

with col1:
    day = st.selectbox("Select Day", ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

with col2:
    time = st.selectbox("Time Slot", ["Morning","Lunch","Evening"])

# ADVANCED MODE
st.markdown("### Advanced Input (Optional)")

use_advanced = st.checkbox("I am at canteen (use real data)")

if use_advanced:
    col3, col4 = st.columns(2)

    with col3:
        students = st.slider("Number of Students", 0, 200)

    with col4:
        queue = st.slider("Queue Length", 0, 50)
else:
    # Default values (auto prediction based on time)
    if time == "Morning":
        students = 30
        queue = 5
    elif time == "Lunch":
        students = 120
        queue = 30
    else:
        students = 70
        queue = 15

# Day mapping
day_map = {"Mon":1,"Tue":2,"Wed":3,"Thu":4,"Fri":5,"Sat":6,"Sun":0}
day_val = day_map[day]

# ---------------- PREDICT ----------------
if st.button("Predict Waiting Time"):

    pred = model.predict([[day_val, students, queue]])
    wait = pred[0]

    if wait < 5:
        rush = "Low"
        color = "green"
    elif wait < 12:
        rush = "Medium"
        color = "orange"
    else:
        rush = "High"
        color = "red"

    st.markdown("### 📊 Prediction Result")

    colA, colB = st.columns(2)

    with colA:
        st.markdown(f"""
        <div class="card">
        <h4>Waiting Time</h4>
        <h2>{wait:.2f} min</h2>
        </div>
        """, unsafe_allow_html=True)

    with colB:
        st.markdown(f"""
        <div class="card">
        <h4>Rush Level</h4>
        <h2 style='color:{color}'>{rush}</h2>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<br><hr>
<center>
<b>Developed by Team Dhurandhar</b><br>
Purushotam | Suman | Rounak | Fareed   <br> Guided By- Rahul Kumar (Ai)
</center> 
""", unsafe_allow_html=True)