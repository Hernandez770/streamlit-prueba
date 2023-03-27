import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="📉",
    layout="wide",)

option = st.sidebar.selectbox(
    'Selecciona la vista:',
    ('Home', 'Visualizaciones','Mapa'), index=0)

st.sidebar.write(option)

datos=pd.read_csv("data/red_recarga_acceso_publico_2021.csv", sep=";")

uploaded_file = st.sidebar.file_uploader("Elige un CSV", type=["csv"])
if option == "Home":

    st.title("Chrysler Building- HOME")
    with st.expander("Descripción del edificio Chrysler - Haz click para expandir"):
        st.write("""
        El Edificio Chrysler es un rascacielos icónico ubicado en la ciudad de Nueva York, en la intersección de la Avenida Lexington y la calle 42. Fue diseñado por el arquitecto William Van Alen y construido en 1930 para la compañía de automóviles Chrysler. Con sus 77 pisos y una altura de 319 metros, fue el edificio más alto del mundo durante 11 meses antes de ser superado por el Empire State Building.

    El diseño del edificio es un ejemplo destacado del estilo art decó, con detalles ornamentales en la fachada, incluyendo gárgolas de acero inoxidable y un capitel de acero niquelado en la cima. En la base del edificio, la entrada principal cuenta con enormes puertas de bronce decoradas con bajorrelieves que representan la industria del automóvil.

    Hoy en día, el Edificio Chrysler sigue siendo uno de los puntos de referencia más reconocidos de la ciudad de Nueva York y es un destino turístico popular. Ha aparecido en numerosas películas, programas de televisión y obras de arte y es considerado uno de los logros más importantes de la arquitectura de rascacielos de la ciudad.
    """)
    image = Image.open('ny.jpeg')

    st.image(image, caption='NEW YORK', width=1000)

    if uploaded_file is not None:
        datos = pd.read_csv(uploaded_file)

    st.write(datos)

    with st.echo():
        #Código para generar números pares
        lista= list(range(10))
        even_list=[x for x in lista if x%2==0]
        st.write(even_list)

elif option == "Mapa":
    datos_mapa = datos[["latidtud","longitud"]]
    datos_mapa.columns = ["lat","lon"]
    st.subheader("Mapa cargadores")
    st.map(datos_mapa)

elif option == "Visualizaciones":
    datos_barchart = datos.groupby("DISTRITO")[["Nº CARGADORES"]].sum().reset_index()
    st.subheader("Nº cargadores por distrito")
    st.bar_chart(datos_barchart, x="DISTRITO", y="Nº CARGADORES")