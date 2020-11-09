# Use your knowledge of linked lists and hashing to create a blockchain implementation.
# Each of these blocks become a node in a linked list.
# SHA256, Greenwich Mean Time (GMT)
import hashlib

class Block:
    # Data: text strings
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.next = None
      self.previous_hash = previous_hash #for linked list
      self.hash = self.calc_hash()
    def calc_hash(self):
        # output: hash value
        # input = data or hash_str? 
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

# what would be the corner cases?    
    # null value
    # large numbers
    # duplicates??
prev_hash = '012938'
block1 = Block('13:27 060620', 'drone', prev_hash)
block2 = Block('12:59 060720', 'vaccuum', prev_hash)
block1.next = block2





