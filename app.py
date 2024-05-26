import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown("""
    <style>
    .stForm {
            background-color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

st.header('Gráficos sobre la venta de autos')
st.write('Selecciona el gráfico con la información que le gustaría consultar')

car_data = pd.read_csv('vehicles_us(2).csv') # leer los datos

hist_check_model = st.checkbox('Construir histograma de modelo de autos')
if hist_check_model:
    st.write('Histograma sobre la venta de autos por modelo')
    fig_m = px.histogram(car_data, x="model")
    st.plotly_chart(fig_m, use_container_width=True)

hist_check_year = st.checkbox('Consultar histograma del año de los autos')
if hist_check_year:
    st.write('Histograma sobre la venta de autos por año del auto')
    fig_y = px.histogram(car_data, x='model_year')
    st.plotly_chart(fig_y, use_container_width=True)

hist_check_price = st.checkbox('Consultar histograma con precios de los autos')
if hist_check_price:
    st.write('Histograma sobre los precios de venta de los autos')
    fig_p = px.histogram(car_data, x='price')
    st.plotly_chart(fig_p, use_container_width=True)

scatter_button = st.button('Consultar diagramas de dispersión')
scatter_check = st.checkbox('Consultar diagrama de dispersión modelo del auto vs año')
if scatter_check:
    st.write('Diagrama de dispersión sobre la venta de modelo de auto vs año')
    fig_m_y = px.scatter(car_data, x='model', y='model_year')
    st.plotly_chart(fig_m_y, use_container_width=True)

scatter_check_p_m = st.checkbox('Consultar diagrama de dispersión sobre el precio del auto vs el model')
if scatter_check_p_m:
    st.write('Diagrama de dispersión de precio de auto a corde a su modelo')
    fig_p_m = px.scatter(car_data, x='model', y='price')
    st.plotly_chart(fig_p_m, use_container_width=True)