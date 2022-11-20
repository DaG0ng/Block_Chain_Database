import streamlit as st
from PIL import Image
import json

st.set_page_config(layout='wide')

row0_1, row0_spacer1, row0_2, row0_spacer2 = st.columns(
    (2, 0.2, 1, 0.1)
)
row0_1.title('Demo Block Chain Base Database')

with row0_2:
    st.write("")
    st.subheader("Created by [DaG0ng](https://github.com/DaG0ng/Block_Chain_Database)")


st.markdown('Hey there, welcome to Da Gong\' Medical Record Block Chain Database👏. This app aims to use block chain technology for sensitive information storage like the medical records here. This page is a demo of the simulation of the Block Chain Database.')

st.subheader('App Introduction')
st.markdown('+  **Home**: The Introduction Page' + '\n' +
            '+  **Admin Entry**: This is the entry which allow user to manipulate the database using admin identity. Admin have full access to the database.' + '\n' +
            '+  **Doctor Entry**: This is the entry which allow user to manipulate the database using doctor identity. Doctor have edit permission for certain patient.' + '\n' +
            '+  **Patient Entry**: This is the entry which allow user to manipulate the database using patient identity. Patient have view permission of their self medical records' + '\n' + 
            '+  **About**: Documentations and Technology Explanation.')

st.subheader('Medical Record Sample')
st.markdown('This is a sample medical record. The Database contains multiple medical records using this format.')
see_dataset1 = st.expander('You can click here to view the medical record sample')
with see_dataset1:
  f = open('samples/1.json')
  otherdeeds_dataset = json.load(f)
  st.json(otherdeeds_dataset)



st.subheader('🔥Block Chain Technology🔥')
with st.container():
  deed1, deed2= st.columns(2)
  with deed1:
    image = Image.open('images/1.jpg')
    st.image(image)
  with deed2:
    image = Image.open('images/2.jpg')
    st.image(image)
 


