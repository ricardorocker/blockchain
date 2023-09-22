import datetime #Every block will have your exacly creation date
import hashlib #Every block will have your hashs
import json #Make json data and read on json

from flask import Flask, jsonify #jsonify(make post requests and receive responses)

# Part 01, create a Blockchain

class Blockchain: #Class creation
    def __init__(self): #Init function, self(class variable refer to own class)
        self.chain = [] #Inicialize array on python
        self.create_block(proof = 1, previous_hash='0') #Method 'create_block'(genesis block) with two parameters
        
    def create_block(self, proof, previous_hash): #Creation 'create_block' method with 3 params, 'self', 'proof', 'previous_hash'
        block = { #Create dictionary with 4 keys
            'index': len(self.chain) + 1, #Index, number of block
            'timestamp': str(datetime.datetime.now()), #Exacly date creation
            'proof': proof, #Proofwork puzle = nonse
            'previous_hash': previous_hash #Link with previous_hash
            }
        self.chain.append(block) #Add this element to Chain array
        return block
    
    def get_previous_block(self): #Creation getPreviouBlock
        return self.chain[-1] #Return Chain array previous