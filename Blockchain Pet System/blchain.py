import datetime
import hashlib
from flask import Flask, request, render_template

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0*0
    timestamp = datetime.datetime.now()
    
    def __init__(self, data, name, age, address, species, eth_address):
        self.data = data
        self.blockName = name
        self.blockAge = age
        self.blockAddress = address
        self.blockSpecies = species
        self.eth_address = eth_address
        
    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf8') +
        str(self.data).encode('utf8') +
        str(self.previous_hash).encode('utf8') +
        str(self.timestamp).encode('utf8') +
        str(self.blockName).encode('utf8') +
        str(self.blockAge).encode('utf8') +
        str(self.blockAddress).encode('utf8') +
        str(self.blockSpecies).encode('utf8') +
        str(self.eth_address).encode('utf8'))
        
        return h.hexdigest()
        
    def __str__(self):
        return f"Block Hash: {str(self.hash())}\nBlockName: {str(self.blockName)}\nBlock Data: {str(self.data)}\nBlock Age: {str(self.blockAge)}\nBlock Address: {str(self.blockAddress)}\nBlock Species: {str(self.blockSpecies)}\nEthereum Address: {str(self.eth_address)}\nHashes: {str(self.nonce)}\n--------------"


class Blockchain:
    diff = 10
    maxNonce = 2**32
    target = 2**(256-diff)
    
    block = Block("Genesis text", "Genesis", "N/A", "N/A", "N/A", "N/A")
    dummy = head = block
    
    def add(self, block):
        block.previous_hash = self.block.hash() 
        self.block.next = block
        self.block = self.block.next
    
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                return block.blockName, block.data, block.blockAge, block.blockAddress, block.blockSpecies, block.eth_address
            else:
                block.nonce += 1
    
    
app = Flask(__name__)
blockchain = Blockchain()
my_dict = []

@app.route('/')
def my_form():
    return render_template('index.html', content="")

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        Petname = request.form.get('Petname')
        Details = request.form.get('Details')
        PetAge = request.form.get('PetAge')
        PetAddress = request.form.get('PetAddress')
        Species = request.form.get('Species')
        eth_address = request.form.get('ethAddress')
        
        nm, tx, age, addr, species, eth = blockchain.mine(Block(Details, Petname, PetAge, PetAddress, Species, eth_address))
        my_dict.append([nm, tx, age, addr, species, eth])
        print(f"Received Ethereum address: {eth_address}")
        return render_template('index.html', name_list=my_dict)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
