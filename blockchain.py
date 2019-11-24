import block
import json
import datetime as date
import hashlib

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.index = 0
        self.last_block: block.Block

    # Make First Block
    def create_genesis_block(self):
        tmp = block.Block(0, date.datetime.now(), block.Data(
            send_key='0', recv_key='0', fileId='0'), '0')
        self.chain.append(tmp)
        self.last_block = tmp
        self.index += 1
    # index, timestamp, data :Data, previous_hash
    # Make Next Block

        
    def next_block(self, data: block.Data) -> block.Block:
        sha = hashlib.sha256()
        sha.update(str(data.body).encode())
        print(self.index,  sha.hexdigest())        
        tmp = block.Block(self.index, date.datetime.now(),
                          data, self.last_block.hash)
        
        if not self.proof(tmp):
            raise Exception("asfd")
        
        tmp.data.transactions = self.last_block.data.transactions                                   
        
        tmp.data.transactions['transactions'].append({
            'sender' : tmp.data.body['sender'],
            'receiver': tmp.data.body['receiver'],
            'index' : tmp.index
        })

        self.chain.append(tmp)          
        for i in self.chain:
            i.data.transactions['transactions'] = tmp.data.transactions['transactions']
            
        self.index += 1
        self.last_block = tmp        
        return tmp

    def proof(self, block :block.Block) -> bool:                
                        
        banded_strs = [' ','0','']
        for banded_str in banded_strs:
            if block.data.body['sender'] in banded_str:
                return False
            if block.data.body['receiver'] in banded_str:
                return False
        return True    
    
    def get_block(self, fileId :str) -> block.Block:        
        
        lsdata = list(range(1, len(self.chain)))
        for i, j in zip( range( len(self.chain)), lsdata):            
            if self.chain[i].hash != self.chain[j].previous_hash:
                raise Exception(1)
        
        for i in self.chain:            
            if i.data.body['fileId'] == fileId:
                return i
        raise Exception(2)
    
    def get_relate_blocks(self, id: str) -> list:
        block_list = []
        for i in self.last_block.data.transactions['transactions'] :            
            if i['sender'] == id or i['receiver'] == id:
                block_list.append(i)
        return block_list