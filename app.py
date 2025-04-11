import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open(r"C:\Users\arshi\OneDrive\Documents\laptop price prediction\pipe (7).pkl",'rb'))
df=pickle.load(open(r"C:\Users\arshi\OneDrive\Documents\laptop price prediction\df (7).pkl",'rb'))

# Set Page Configuration
st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

# Initialize session state
if "show_prediction" not in st.session_state:
    st.session_state.show_prediction = False

# Welcome Page
if not st.session_state.show_prediction:
    st.markdown("""
        <style>
          
html, body, .stApp {
    background: url("https://images.pexels.com/photos/5706032/pexels-photo-5706032.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2") no-repeat center center fixed;
    
    background-size: cover;
    font-family: 'Segoe UI', sans-serif;
}

            .main {
                background-color: white;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                margin: 50px auto;
                max-width: 700px;
                text-align: center;
            }

            .title {
                font-size: 48px;
                font-weight: 700;
                color: #2c3e50;
                margin-bottom: 10px;
                animation: fadeIn 1.5s ease-in-out;
            }

            .subtitle {
                font-size: 20px;
                color: #555;
                margin-bottom: 30px;
            }

            .predict-btn {
                background-color: #1abc9c;
                color: white;
                font-size: 18px;
                padding: 14px 35px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: background 0.3s ease;
            }

            .predict-btn:hover {
                background-color: #16a085;
            }

            .form-section {
                text-align: left;
                margin-top: 20px;
            }

            .form-section label {
                font-weight: 600;
                color: #34495e;
            }

            .result-box {
                background-color: #dff9fb;
                color: #130f40;
                padding: 20px;
                font-size: 24px;
                font-weight: bold;
                border-radius: 12px;
                margin-top: 30px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.05);
                animation: fadeInUp 1s ease-in-out;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px);}
                to { opacity: 1; transform: translateY(0);}
            }

            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(40px);}
                to { opacity: 1; transform: translateY(0);}
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">🔍 Laptop Price Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">✨Predict the cost of your dream Lap!</div>',
                unsafe_allow_html=True)

    if st.button("🚀 Start Prediction", key="start", help="Click to start"):
        st.session_state.show_prediction = True
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# Prediction Page
if st.session_state.show_prediction:
    st.title("💻 Laptop Price Prediction")

    company = st.selectbox('Brand', ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'MSI', 'Toshiba'])
    type = st.selectbox('Type', ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Workstation'])
    ram = st.selectbox('RAM (GB)', [4, 8, 16, 32, 64])
    weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, step=0.1)
    touchscreen = st.radio('Touchscreen', ['Yes', 'No'])
    ips = st.radio('IPS Display', ['Yes', 'No'])
    screen_size = st.number_input('Screen Size (inches)', min_value=10.0, max_value=20.0, step=0.1)
    resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '3840x2160', '3200x1800'])
    cpu = st.selectbox('Processor', ['Intel Core i3', 'Intel Core i5', 'Intel Core i7'])
    hdd = st.selectbox('HDD (GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox('SSD (GB)', [0, 128, 256, 512, 1024])
    gpu = st.selectbox('GPU', ['Intel', 'AMD', 'Nvidia'])
    os = st.selectbox('Operating System', ['Windows'])

    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    res_x, res_y = map(int, resolution.split('x'))
    ppi = ((res_x**2 + res_y**2) ** 0.5) / screen_size

    query = np.array([[company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]], dtype=object)

    # Predict button
    if st.button('Predict Price'):
        predicted_price = round(np.exp(pipe.predict(query)[0]))
        st.success(f"💰 **Predicted Laptop Price: ₹{predicted_price}**")