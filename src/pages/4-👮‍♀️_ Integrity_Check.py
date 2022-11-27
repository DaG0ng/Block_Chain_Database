import streamlit as st
from PIL import Image
import json
from blockchain import Block
from blockchain import Blockchain
import pandas as pd
import numpy as np
import copy

st.set_page_config(layout='wide')
st.title('Integrity Check')
st.subheader("Show that illegal action to database will be found out easily")

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def bind_socket():
    blockchain = Blockchain()
    return blockchain

blockchain=copy.deepcopy(bind_socket())

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def initial_load(blockchain):
    st.caption("Creating block chain Database")
    st.caption("Adding medical records block chain Database")
    f = open('../samples/1.json')
    data = json.load(f)
    blockchain.add_new_data(data)
    blockchain.mine()
    f = open('../samples/2.json')
    data = json.load(f)
    blockchain.add_new_data(data)
    blockchain.mine()
    f = open('../samples/3.json')
    data = json.load(f)
    blockchain.add_new_data(data)
    blockchain.mine()
    st.caption("Finish Initializing the Database")
    return blockchain

blockchain=initial_load(blockchain)

number_of_editing = st.slider('Edit which block of data?', 1, len(blockchain.chain)-1, 1)
editing_text=blockchain.chain[number_of_editing].data
edit_input = st.text_input('Edit current medical records in json format', json.dumps(editing_text))
def editing(blockchain, number_of_editing, record_input):
    blockchain.chain[number_of_editing].data=json.loads(record_input)
    return blockchain

if st.button('Edit this Block Illegally'):
    with st.expander("Show Process"):
        blockchain=editing(blockchain, number_of_editing, edit_input)


if st.button('Check Integrity'):
    blockchain.verify_integrity()