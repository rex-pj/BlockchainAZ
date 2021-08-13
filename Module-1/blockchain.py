import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building a blockchain

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
    
    def create_block(self, proof, previous_hash):
        currentIndex = len(self.chain) + 1
        currentTimestamp = str(datetime.datetime.now())
        block = { 'index': currentIndex, 
            'timestamp': currentTimestamp, 
            'proof': proof,
            'previous_hash': previous_hash
            }
        
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        