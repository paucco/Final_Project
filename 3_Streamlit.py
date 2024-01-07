import pandas as pd
import streamlit as st

from joblib import load

# Cargamos el modelo entrenado y el df
rfr_best_model = load('best_model.joblib')
df = load('cont_bcn_eixample_18_23_ML.df')

# Configuración de Streamlit
st.title('Prediction of pollution in the center of Barcelona (Eixample)')

year = st.number_input('Year', min_value=1, max_value=2100, step=1)
month = st.number_input('Month', min_value=1, max_value=12, step=1)
day = st.number_input('Day', min_value=1, max_value=31, step=1)
CO = st.slider('CO', min_value=df['CO'].min(), max_value=df['CO'].max(), step=0.10)
NO = st.slider('NO', min_value=df['NO'].min(), max_value=df['NO'].max(), step=5)
O3 = st.slider('O₃', min_value=df['O3'].min(), max_value=df['O3'].max(), step=5)
PM10 = st.slider('PM10', min_value=df['PM10'].min(), max_value=df['PM10'].max(), step=5)
SO2 = st.slider('SO₂', min_value=df['SO2'].min(), max_value=df['SO2'].max(), step=0.50)



if st.button('What concentration will NO₂ have in the predicted year?'):
    
    # Creamos un DataFrame con los datos ingresados por el usuario
    input_data = pd.DataFrame([[year, month, day, CO, NO, O3, PM10, SO2]],
                           columns=df.drop(['NO2', 'season_spring', 'season_summer', 'season_winter'], axis=1).columns)

    predict = rfr_best_model.predict(input_data)[0]
    st.write(f"The predicted concentration of NO₂ is {str(predict)} µg/m³")
 