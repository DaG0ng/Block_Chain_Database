import streamlit as st
import hashlib
import json
import time
from timeit import default_timer as timer
from datetime import timedelta
import random
import string
import copy

class Block:
    def __init__(self, index, data, timestamp, previous_hash, nonce=0):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return 'Block: {}'.format(self.__dict__)



class Blockchain:
    def __init__(self):
        self.new_data = []
        self.chain = []
        self.difficulty = 1
        self.__create_genesis_block()

        
    def __create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_new_data(self, data):
        self.new_data.append(data)

    def mine(self):
        if not self.new_data:
            return False
        last_block = self.last_block
        new_block = Block(index=last_block.index + 1,
                          data=self.new_data,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)
        proof = self.__proof_of_work(new_block)
        self.__add_block(new_block, proof)
        self.new_data = []
        return new_block.index

    @property
    def last_block(self):
        return self.chain[-1]
    
    def __proof_of_work(self, block):
        start = timer()
        block.nonce = 0
        computed_hash = block.compute_hash()
        st.caption('Mining block {}'.format(block.index))
        st.caption('Difficulty: {}'.format(self.difficulty))
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        st.caption('Computed hash: {}'.format(computed_hash))
        st.caption('Nonce: {}'.format(block.nonce))
        end = timer()
        st.caption('Elapsed time: {}'.format(timedelta(seconds=end - start)))
        return computed_hash

    def __is_valid_proof(self, block, block_hash):
        return block_hash.startswith('0' * self.difficulty) and block_hash == block.compute_hash()

    def __add_block(self, block, proof):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.__is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
    
    def verify_integrity(self):
        for i in self.chain:
            temp=copy.deepcopy(i)
            del temp.hash
            if temp.compute_hash()!=i.hash:
                st.caption("Integrity Failed")
                st.caption("Block {} got unverified change.".format(temp.index))
                return False
        for i in range(1,len(self.chain)-1):
            if self.chain[i].previous_hash!=self.chain[i-1].hash:
                st.caption("Integrity Failed")
                return False
        st.caption("Integrity Ensured")
        return True
    
    def view_by_hash_code(self, hash_code):
        for i in self.chain:
            if hash_code==i.hash:
                return i.data
        st.caption("Nothing fit your search")
        
    def edit_by_hash_code(self, hash_code, new_data):
        delete_blocks=0
        for i in self.chain:
            if hash_code==i.hash:
                delete_blocks=i.index
                break
        temp_chain=self.chain[delete_blocks+1:]
        self.chain=self.chain[:delete_blocks]
        self.add_new_data(new_data)
        self.mine()
        for i in temp_chain:
            self.add_new_data(i.data)
            self.mine()
    
    def edit_by_index(self, index, new_data):
        delete_blocks=index
        temp_chain=self.chain[delete_blocks+1:]
        self.chain=self.chain[:delete_blocks]
        self.add_new_data(new_data)
        self.mine()
        for i in temp_chain:
            self.add_new_data(i.data)
            self.mine()

    def delete_by_index(self, index):
        delete_blocks=index
        temp_chain=self.chain[delete_blocks+1:]
        self.chain=self.chain[:delete_blocks]
        for i in temp_chain:
            self.add_new_data(i.data)
            self.mine()