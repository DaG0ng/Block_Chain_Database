import streamlit as st
from PIL import Image
import json
from blockchain import Block
from blockchain import Blockchain
import pandas as pd
import numpy as np
import copy

st.set_page_config(layout='wide')
st.title('Patient Entry')
st.subheader("Use Patient Identity to Checking the self medical records")

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def bind_socket():
    blockchain = Blockchain()
    return blockchain

blockchain=copy.deepcopy(bind_socket())

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

st.caption("Cheating Hash Keys List:")
st.caption(blockchain.chain[1].hash)
st.caption(blockchain.chain[2].hash)
st.caption(blockchain.chain[3].hash)

st.header("Checking Certain Patient Medical Record Using private key")
hash_key = st.text_input('Hash Key')

if st.button('Check this Patient'):
    st.write(blockchain.view_by_hash_code(hash_key))