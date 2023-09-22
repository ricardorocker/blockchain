import datetime #Every block will have your exacly creation date
import hashlib #Every block will have your hashs
import json #Make json data and read on json

from flask import Flask, jsonify #jsonify(make post requests and receive responses)

# Part 01, create a Blockchain

class Blockchain: #Class creation
    def __init__(self): #Init function, self(class variable refer to own class)
        self.chain = [] #Inicialize array on python
        self.create_block(proof = 1, previous_has='0') #Method 'create_block'(genesis block) with two parameters