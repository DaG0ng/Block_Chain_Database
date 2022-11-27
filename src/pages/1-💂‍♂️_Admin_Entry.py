import streamlit as st
from PIL import Image
import json
from blockchain import Block
from blockchain import Blockchain
import pandas as pd
import numpy as np
import copy
import time

st.set_page_config(layout='wide')
st.title('Admin Entry')
st.subheader("Use Admin Identity to Manage the distributed Block Chain Database")
@st.cache
def get_time():
    created_time=time.asctime()
    return created_time

created_time=get_time()
latest_time=time.asctime()

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def bind_socket():
    blockchain = Blockchain()
    return blockchain
st.write('***')
blockchain=copy.deepcopy(bind_socket())
st.write("Initializing")

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def initial_load(blockchain):
    st.caption("Creating block chain Database")
    st.caption("Adding medical records block chain Database")
    f = open('../../samples/1.json')
    data = json.load(f)
    blockchain.add_new_data(data)
    blockchain.mine()
    f = open('../../samples/2.json')
    data = json.load(f)
    blockchain.add_new_data(data)
    blockchain.mine()
    f = open('../../samples/3.json')
    data = json.load(f)
    blockchain.add_new_data(data)
    blockchain.mine()
    st.caption("Finish Initializing the Database")
    return blockchain


blockchain=initial_load(blockchain)

st.write("The initial database have three medical records so four blocks in total.")
number_of_checking = st.slider('Check which block of data?', 0, len(blockchain.chain)-1, 1)
st.json(blockchain.chain[number_of_checking].__dict__)    

def bind_socket2(blockchain, record_input):
    input_json=json.dumps(record_input)
    blockchain.add_new_data(input_json)
    blockchain.mine()
    return blockchain

st.write('***')
text_input = st.text_input('Add more medical records in json format', '{"name":"Example Input","age":34,"medical condition":"Example Input"}')
if st.button('Add into Database'):
    with st.expander("Show Process"):
        blockchain=bind_socket2(blockchain, text_input)
        latest_time=time.asctime()




st.write('***')
number_of_editing = st.slider('Edit which block of data?', 1, len(blockchain.chain)-1, 1)
editing_text=blockchain.chain[number_of_editing].data

edit_input = st.text_input('Edit current medical records in json format', editing_text)
def editing(blockchain, number_of_editing, record_input):
    input_json=json.dumps(record_input)
    blockchain.edit_by_index(number_of_editing, record_input)
    return blockchain

if st.button('Edit this Block'):
    with st.expander("Show Process"):
        blockchain=editing(blockchain, number_of_editing, edit_input)
        latest_time=time.asctime()


st.write('***')
number_of_deleting = st.slider('Delete which block of data?', 1, len(blockchain.chain)-1, 1)

def deleting(blockchain, number_of_deleting):
    blockchain.delete_by_index(number_of_deleting)
    return blockchain

if st.button('Delete this Block'):
    with st.expander("Show Process"):
        blockchain=deleting(blockchain, number_of_deleting)
        latest_time=time.asctime()

st.write('***')
col1, col2, col3 = st.columns(3)
col1.metric("Number of Blocks in Database", len(blockchain.chain))
col2.metric("Latest Editing Time", latest_time)
col3.metric("Database Created Time", created_time)

st.caption("Due to the fact that Block Chain Database can be decentraliazed. The data in the database can be distributed into several different locations for storage.")
st.caption("The data is storing in unit of block.")

