import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Canteen Predictor", layout="centered")

# ---------------- TOGGLE ----------------
dark_mode = st.toggle("🌙 Dark Mode")

# ---------------- CSS ----------------
if dark_mode:
    bg_color = "#111827"
    text_color = "#f9fafb"
    card_color = "#1f2937"
    title_color = "#60a5fa"
else:
    bg_color = "#f9fafb"
    text_color = "#1f2937"
    card_color = "#ffffff"
    title_color = "#2563eb"

st.markdown(f"""
<style>

/* Background */
.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}

/* Main box */
.main-box {{
    background: {card_color};
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
}}

/* Title */
.title {{
    text-align: center;
    font-size: 32px;
    font-weight: 600;
    color: {title_color};
}}

/* Subtitle */
.subtitle {{
    text-align: center;
    color: gray;
    margin-bottom: 15px;
}}

/* Card */
.card {{
    background: {card_color};
    padding: 18px;
    border-radius: 10px;
    text-align: center;
    transition: 0.25s;
}}

/* Hover effect (soft) */
.card:hover {{
    transform: translateY(-4px);
    box-shadow: 0px 6px 12px rgba(0,0,0,0.12);
}}

/* Button */
.stButton>button {{
    width: 100%;
    background-color: {title_color};
    color: white;
    border-radius: 8px;
    height: 42px;
    border: none;
}}

.stButton>button:hover {{
    opacity: 0.9;
}}

/* Footer */
.footer {{
    text-align: center;
    margin-top: 30px;
    font-size: 18px;
    color: gray;
}}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">Smart Canteen Queue Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Vaishali Food Park</div>', unsafe_allow_html=True)

st.write("")

# ---------------- INPUT ----------------
st.markdown('<div class="main-box">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    day = st.selectbox("Day", ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

with col2:
    students = st.slider("Students", 0, 100)

queue = st.slider("Queue Length", 0, 50)

# Convert day
day_map = {"Mon":1,"Tue":2,"Wed":3,"Thu":4,"Fri":5,"Sat":6,"Sun":0}
day_val = day_map[day]

st.write("")

# ---------------- BUTTON ----------------
if st.button("Predict"):

    pred = model.predict([[day_val, students, queue]])
    wait = pred[0]

    if wait < 5:
        rush = "Low"
        color = "#16a34a"
    elif wait < 12:
        rush = "Medium"
        color = "#d97706"
    else:
        rush = "High"
        color = "#dc2626"

    st.write("")

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
            <h2 style="color:{color}">{rush}</h2>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
Developed by - Team Dhurandhar<br>
Team Mates: Purushotam, Suman, Rounak, Fareed <br>
            Guided by -Rahul kumar (AI)
</div>
""", unsafe_allow_html=True)