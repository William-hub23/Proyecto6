import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Analisis Vehiculos Sprint 6')

hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un grafico de dispersion')
if build_scatter: # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un grafico de dispercion para el conjunto de datos de anuncios de venta de coches')
            
    # crear un grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)