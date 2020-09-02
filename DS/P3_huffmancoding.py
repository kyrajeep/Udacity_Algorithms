import sys
'''
 huffman tree:
1. nodes as weights. build a min heap. I am so excited.
2. take out two smallest nodes
3. combine them to make an internal node.
'''
#a min heap is used as a priority queue to pop the 
#smallest node at the root
class node_huffman:
    '''
    The node class with the left and right child.
    '''
    def __init__(self,letter):
        self.letter = letter   
        self.weight = 1
        self.left = None
        self.right = None
    #def dummy():
       # a test to see how this class is imported
       
       # print("hello, test")
    def count(self,data):
        pass
        # this function counts how many times the letter
        # appeared in the list. Assign the frequency to the 
        # weight variable and return the frequency.
        counter = data.count(self.letter)
        self.weight = counter
        return counter
'''
class huffman_tree:
    # note to self: Does it make sense to build this with a list?
    def __init__(self):
        self.root = None
    
    def insert():
        # the edges are represented as the children
        
    def remove():
        
        if self.root.left >= self.root.right:
            new_node_freq = self.root.frequency + self.root.right.frequency
        # how do you compare and reorganize the hierarchy effectively?
        new_root = self.root.left
        self.root = self.root.left
        self.root.left = new_root.left
        self.root.right = new_root.right
        else:
        new_root = self.root.right
        self.root = self.root.right
        self.root.left = new_root.left
        self.root.right = new_root.right
    def heapify():
        if self.root >= 
        
'''        
# solution
def huffman_encoding(data):
    pass
    #input: a string (data)
    #output: encoded data and its tree
    
    # convert the string into a list
    
    
    tree = huffman_tree()
    # sort data and make it into a tree
    #tree.append(createnode(data))
    return tree
def create_node(data):
    #input: given data, usually a sentence
    #output: node objects used to build a tree
    data = list(data)
    letterlist = []
    all_nodes = dict()
    for i in data:
        if i not in letterlist:
            letterlist.append(i)
            # i-th node is in the all_nodes list
            all_nodes[i] = node_huffman(str(i))
            
        else:
            cur_node = all_nodes[i]
            cur_node.weight += 1
            
    return all_nodes, letterlist


def huffman_decoding(data,tree):
    #output: decoded data
    pass

data = 'I am a big giant tree'
#print(createnode(data))
'''
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
'''
print(create_node(data))
