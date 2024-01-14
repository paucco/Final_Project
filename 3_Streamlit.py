import pandas as pd
import streamlit as st

from joblib import load

# Cargamos el modelo entrenado y el df
rfr_best_model = load('best_model.joblib')
df = pd.read_csv('cont_bcn_eixample_18_23_ML.csv')

# Configuración de Streamlit
st.title('Prediction of pollution in the city center of Barcelona (Eixample)')
st.divider()

st.image('NO2.png')

st.divider()
st.caption('Enter the date')

year = st.number_input('Year', min_value=1, max_value=2100, step=1)
month = st.number_input('Month', min_value=1, max_value=12, step=1)
day = st.number_input('Day', min_value=1, max_value=31, step=1)

st.caption("Enter the concentration of pollutants")

CO = st.slider('CO', min_value=0.0, max_value=3.0, step=0.10)
NO = st.slider('NO', min_value=0.0, max_value=230.0, step=5.0)
O3 = st.slider('O₃', min_value=0.0, max_value=230.0, step=5.0)
PM10 = st.slider('PM10', min_value=0.0, max_value=230.0, step=5.0)
SO2 = st.slider('SO₂', min_value=0.0, max_value=15.0, step=0.50)

season_spring = 1
season_summer = 0
season_winter = 0

st.divider()

if st.button('What concentration will NO₂ have on the date you have chosen?'):
    
    # Creamos un DataFrame con los datos ingresados por el usuario
    input_data = pd.DataFrame([[year, month, day, CO, NO, O3, PM10, SO2, season_spring, season_summer, season_winter]],
                           columns=df.drop(['NO2'], axis=1).columns)

    predict = rfr_best_model.predict(input_data)[0]
    st.metric(label=f"The predicted concentration of NO₂ in {year}", value=f"{predict.round(2)} µg/m³")