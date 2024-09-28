import streamlit as st
import pickle
import matplotlib.pyplot as plt
import os

# Load the model
model = pickle.load(open('RF_price_predicting_model.pkl', 'rb'))
fuel_path = r".\fuel.png"
print("path",os.getcwd())

# Store trials (parameters and predicted price)
if 'trials' not in st.session_state:
    st.session_state.trials = []

# Custom CSS for UI and card layout
st.markdown("""
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: #f0f0f0;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #FF6F61;
        margin-bottom: 20px;
        text-align: center;
    }
    .card-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .card {
        background-color: #333333;
        padding: 15px;
        border-radius: 10px;
        margin: 10px;
        width: 22%;
        color: #f0f0f0;
    }
    .card-title {
        font-size: 18px;
        font-weight: bold;
        color: #FF6F61;
    }
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap'); /* Import Orbitron font */


    .result-box {
        background-color: #444444;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
    }
    .result-price {
        font-size: 32px;
        font-weight: bold;
        color: #FF6F61;
    }
            .glow-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        box-shadow: 0 0 15px red, 0 0 30px red, 0 0 45px red;
        border-radius: 10px;
    }
            .gauge {
  width: 200px;
  height: 100px;
  background-color: #e0e0e0;
  border-radius: 100px 100px 0 0;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.gauge__meter {
  width: 100%;
  height: 100%;
  position: relative;
}

.gauge__fill {
  width: 100%;
  height: 100%;
  background: conic-gradient(#4caf50 0deg, #ff5722 180deg, #f44336 360deg);
  transform: rotate(-90deg);
  transform-origin: center bottom;
  animation: fill-animation 3s forwards;
}

.gauge__cover {
  width: 80%;
  height: 160%;
  background-color: white;
  border-radius: 100%;
  position: absolute;
  top: 20%;
  left: 10%;
}

@keyframes fill-animation {
  from {
    transform: rotate(-90deg);
  }
  to {
    transform: rotate(90deg); /* Adjust the degree here for the desired final gauge position */
  }
}
    </style>
""", unsafe_allow_html=True)

# Sidebar form input
with st.sidebar:
   
    image_path = "https://img.freepik.com/free-photo/closeup-shot-front-blue-modern-stylish-car_181624-11795.jpg?t=st=1727429063~exp=1727432663~hmac=8b5ba870d19d89b1fe833b4cb938c4c2bfbd30eab1960a1dbc1f9075ddeb8d72&w=740"


   
    st.sidebar.markdown(
    f'<img src="{image_path}" style="width:100%; height:auto;" class ="glow-img">',
    unsafe_allow_html=True
                            )


# Create columns for the form
    col1, col2 = st.columns(2)

        # First group of inputs
    with col1:
            # Car Purchase Year
            year = st.number_input("Car Purchase Year", min_value=1990, max_value=2024, step=1)
            Years_old = 2024-year
            # Kilometers Driven
            Kms_Driven = st.number_input("Kilometers Driven", min_value=0, step=500)

            # Fuel Type
            Fuel_Type_Petrol_input = st.selectbox("Fuel Type", ["Petrol", "Diesel",'CNG'])
            if(Fuel_Type_Petrol_input=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
            elif(Fuel_Type_Petrol_input=='Diesel'):
                Fuel_Type_Petrol=0
                Fuel_Type_Diesel=1
            else:
                Fuel_Type_Petrol=0
                Fuel_Type_Diesel=0

        # Second group of inputs
    with col2:
            # Present Price of the car
            Present_Price = st.number_input("Present Price (in lakhs)", min_value=0.0, max_value=100.0, step=0.1)

            # Transmission type
            Transmission_Mannual_input = st.selectbox("Transmission", ["Manual", "Automatic"])
            if(Transmission_Mannual_input=='Mannual'):
                Transmission_Mannual=1
            else:
                Transmission_Mannual=0


            # Owner number
            Owner = st.selectbox("Previous Owners", [0, 1, 2, 3])

        # Seller Type outside columns
    Seller_Type_Individual = st.selectbox("Seller Type", ["Dealer", "Individual"])
    if(Seller_Type_Individual=='Individual'):
                Seller_Type_Individual=1
    else:
                Seller_Type_Individual=0	


# Title
st.markdown('<div class="title">Car Dekho: Sell Your Car</div>', unsafe_allow_html=True)

# Display parameter cards dynamically as values are selected
st.subheader("Selected Parameters")

import streamlit as st

def display_parameters(year, kms, fuel, price, transmission, owner, seller, years_old):
    # CSS styling for the cards and grid layout
    st.markdown("""
    <style>
    .card-container {
        display: flex;
        grid-template-columns: repeat(4, 1fr); /* 4 cards per row */
        gap: 10px; /* space between cards */
        margin-bottom: 20px;
    }
    .card {
        background-color: #333333;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        width:200px;
    }
    .card-title {
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 5px;
    }
    
    .card-value {
        font-size: 25px;
        color: #ffffff;
      
        font-family: 'Lucida Console', Monaco, monospace;
    }
    </style>
    """, unsafe_allow_html=True)

    # Markup for the card content
    st.markdown(f"""
        <div class="card-container">
            <div class="card">
                <div class="card-title">Car Purchase Year</div>
                <img class="glow-img" src="https://img.freepik.com/premium-photo/calendar-icon_861346-91069.jpg?w=740">
                <div class="card-value">{year} Model</div>
            </div>
            <div class="card">
                <div class="card-title">Kilometers Driven</div>
                <img class ="glow-img" src="https://img.freepik.com/free-vector/black-blue-speedometer_1057-3274.jpg?t=st=1727454652~exp=1727458252~hmac=93a0437fa865a4190bcb1cf0d3271e95a355eafbc55dec3cb7a24b899b5eb203&w=740">
                <div class="card-value">{kms} km</div>
                </div>
            <div class="card">
                <div class="card-title">Fuel Type</div>
                <img class="glow-img"  src="https://img.freepik.com/premium-vector/fuel-indicator-icon_717549-2090.jpg?w=740">
                <div class="card-value">{fuel}</div>
            </div>
            <div class="card">
                <div class="card-title">Present Price</div>
                <img class ="glow-img" src="https://img.freepik.com/free-vector/indian-rupee-money-bag_23-2147994831.jpg?t=st=1727455006~exp=1727458606~hmac=9ee0c46dab56fdc927f647fd92b8e6d419442a00e28947f85388d96b4e7f0f3c&w=740">
                <div class="card-value">{price} lakhs</div>
            </div>
            <div class="card">
                <div class="card-title">Transmission</div>
                <img class= "glow-img" src ="https://img.freepik.com/free-vector/metal-gears_1284-670.jpg?t=st=1727454805~exp=1727458405~hmac=b9aa4122adb7d2e1a3a87c150104bee1546cf8e07e932196f28be70d39be0d8a&w=740">
                <div class="card-value">{transmission}</div>
            </div>
            <div class="card">
                <div class="card-title">Previous Owners</div>
                <img class="glow-img" src="https://img.freepik.com/premium-photo/portrait-people-happy-with-purchase-expensive-new-car-vector-illustration_1077802-383511.jpg?w=740">
                <div class="card-value">{owner}</div>
             </div>
            
        </div>
    """, unsafe_allow_html=True)


    #st.markdown('</div>', unsafe_allow_html=True)

display_parameters(year, Kms_Driven, Fuel_Type_Petrol_input, Present_Price, Transmission_Mannual_input, Owner, Seller_Type_Individual, Years_old)

# Prediction Button
if st.sidebar.button("Predict Price"):
    try:
        # Predict price
        prediction = model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual ]])
        output = round(prediction[0], 2)
        
        # Save the current trial data
        trial_data = {
            'year': year,
            'kms': Kms_Driven,
            'price': Present_Price,
            'predicted_price': output
        }
        st.session_state.trials.append(trial_data)

        # Display result card
        st.markdown(f'<div class="result-box"><div class="result-price">Estimated Price: {output} lakhs 🙌</div></div>', unsafe_allow_html=True)

        # Display comparison graph
        st.subheader("Parameter Trials Comparison")

        if len(st.session_state.trials) > 0:
            # Plot graph for all trials
            fig, ax = plt.subplots()
            ax.set_facecolor('#1e1e1e')
            fig.patch.set_facecolor('#1e1e1e')
           

            plt.grid(True, which='both', axis='both', linestyle='--', color='#555555')
            plt.legend(loc='upper right')

            for idx, trial in enumerate(st.session_state.trials):
                params = ['Present_Price', 'Kms_Driven', 'Years_old']
                values = [trial['price'], trial['kms'], 2024 - trial['year']]
                ax.plot(params, values, marker='o', linestyle='-', label=f'Trial {idx+1}: Pred Price {trial["predicted_price"]} lakhs')

            ax.set_xlabel('Parameters',color='#f0f0f0')
            ax.set_ylabel('Values',color='#f0f0f0')
            ax.set_title('Trials Comparison: Parameters vs. Predicted Price',color='#FF6F61')
            ax.tick_params(axis='x', colors='#ffffff')  # Set color of x-axis tick values
            ax.tick_params(axis='y', colors='#ffffff') 
            ax.legend()

            st.pyplot(fig)

    except Exception as e:
        st.error(f"Oops! Something went wrong. {str(e)}")
