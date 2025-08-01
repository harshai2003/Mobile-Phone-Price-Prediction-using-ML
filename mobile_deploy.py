import streamlit as st
import numpy as np
import pickle
import base64

# --- Set Background ---
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        .blur-box {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 2rem;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }}

        label, h1, h3, p {{
            color: white !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# Set background image
set_background("phone_pics.jpg")  # <-- Replace with your actual image file name

# --- Load Model ---
with open("rf_model.pkl", "rb") as file:
    model = pickle.load(file)

# --- Title ---
st.markdown("<h1 style='text-align: center;'>📱 Mobile Price Prediction</h1>", unsafe_allow_html=True)
st.write("Predict the price range of a mobile based on its specifications.")

# --- Input Section with Blur Box ---
with st.container():
    st.markdown('<div class="blur-box">', unsafe_allow_html=True)

    battery_power = st.slider("Battery Power (mAh)", 500, 2000, 1000)
    blue = st.number_input("Bluetooth", 0, 1, 1)
    clock_speed = st.number_input("Clock Speed (GHz)", 0.5, 3.0, 1.5, step=0.1)
    dual_sim = st.number_input("Dual SIM", 0, 1, 1)
    fc = st.number_input("Front Camera (MP)", 0, 20, 0)
    four_g = st.number_input("4G", 0, 1, 1)
    int_memory = st.number_input("Internal Memory (GB)", 1, 128, 32)
    m_deep = st.number_input("Mobile Depth (cm)", 0.1, 1.0, 0.5, step=0.1)
    mobile_wt = st.number_input("Mobile Weight (g)", 80, 250, 150)
    n_cores = st.number_input("Number of Cores", 1, 8, 4)
    pc = st.number_input("Primary Camera (MP)", 0, 20, 10)
    px_height = st.number_input("Pixel Height", 0, 1960, 1000)
    px_width = st.number_input("Pixel Width", 500, 2000, 1000)
    ram = st.number_input("RAM (MB)", 256, 8196, 4096)
    sc_h = st.number_input("Screen Height (cm)", 5, 20, 10)
    sc_w = st.number_input("Screen Width (cm)", 2, 10, 5)
    talk_time = st.number_input("Talk Time (Hours)", 2, 20, 10)
    three_g = st.number_input("3G", 0, 1, 1)
    touch_screen = st.number_input("Touch Screen", 0, 1, 1)
    wifi = st.number_input("WiFi", 0, 1, 1)

    st.markdown('</div>', unsafe_allow_html=True)

# --- Prediction Button ---
if st.button("Predict Price Category"):
    features = np.array([[battery_power, blue, clock_speed, dual_sim, fc, four_g,
                          int_memory, m_deep, mobile_wt, n_cores, pc, px_height,
                          px_width, ram, sc_h, sc_w, talk_time, three_g,
                          touch_screen, wifi]])
    prediction = model.predict(features)[0]
    categories = ["Low cost", "Medium cost", "High cost", "Very High cost"]
    st.success(f"💰 Predicted Price Category: {categories[prediction]}")
