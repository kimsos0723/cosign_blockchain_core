from flask import Flask, request
import json
import hashlib

import blockchain
import block
app = Flask(__name__)

bc = blockchain.Blockchain()
bc.create_genesis_block()

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!!'
@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        try:            
            bc.next_block(block.Data(
                str(request.args['send']),
                str(request.args['recv']),
                str(request.args['fileId'])
            ))
        except:
            return "can't make new block"
        return 'good'

@app.route('/block_fileId',methods=['GET'])
def select_block_data():
    if request.method == 'GET':
        try:
            i = bc.get_block(str(request.args.get('index')))            
            return json.dumps(i.data.body)
        except:
            return "can't get block", 500

@app.route('/block_relate_block',methods=['GET'])
def select_relate_block_data():
    if request.method == 'GET':
        i = bc.get_relate_blocks(str(request.args.get('srelate')))            
        
        return str(i)

@app.route('/proof', methods=['GET'])
def proof():
    if request.method == 'GET':
        sender = request.args.get('send')
        recver = request.args.get('recv')
        fileId = request.args.get('fileId')
        i = bc.get_block(fileId)
        if i.data.body['sender']  == sender and i.data.body['receiver'] == recver:
            return 'Proofed'
        else:
            return 'ERR', 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
    pass