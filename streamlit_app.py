import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Joseph Santiago Portilla, Ing.')

st.info('Ingeniero Electrónico. Estudiante MSc. en Educación. Ciclista de bajo rendimiento')

icon_size = 20

st_button('portafolio', 'https://joeportilla.ml/portfolio', 'Mira mi portafolio', icon_size)
st_button('kaggle', 'https://www.kaggle.com/joeportilla', 'Mis Notebooks en Kaggle', icon_size)
st_button('github', 'https://github.com/JoePortilla', 'Sigueme en GitHub', icon_size)
st_button('twitter', 'https://twitter.com/JoePortilla', 'Sigueme en Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/PortillaJoe', 'Sigueme en LinkedIn', icon_size)
