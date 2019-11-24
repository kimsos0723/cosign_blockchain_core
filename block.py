import hashlib
import time


class NotProof(Exception):
    """Raised when the input value is """
    pass

class Data:
    def __init__(self, send_key :str, recv_key :str, fileId :str):
        self.transactions = {'transactions' : []}

        self.body = {
            'sender' : send_key,
            'receiver' : recv_key,
            'fileId' : fileId
        }
        
class Block:
    def __init__(self, index, timestamp, data :Data, previous_hash):        
        if(not self.proof(data)):            
            exit(1)
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.hash_block()            
        self.index = index

    def hash_block(self):
        sha = hashlib.sha512()
        sha.update((
            str(self.data.body) +
            str(self.previous_hash)).encode()
        )
        return sha.hexdigest()    
    
    def get_hash(self):
        return self.hash    


    def proof(self, data :Data) -> bool:        
        if data.body['sender'] and data.body['receiver'] :
            return True
        else:
            return False