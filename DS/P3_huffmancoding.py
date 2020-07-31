import sys
'''
 huffman tree:
1. nodes as weights. build a min heap. I am so excited.
2. take out two smallest nodes
3. combine them to make an internal node.
'''
class node_huffman:
    def __init__(self,letter):
        self.letter = letter   
        self.weight = 0
        self.left_c = None
        self.right_c = None
    #def dummy():
        # a test to see how this class is imported
       
       # print("hello, test")
    def count(self,data):
        counter = data.count(self.letter)
        self.weight = counter
        return counter

class huffman_tree:
    def __init__(self):
        self.root = None
    
    def insert(node):
        pass
    def remove():
        pass
    def priority():
        pass
        #sort the nodes according to frequency
    def heapify():
        pass
def huffman_encoding(data):
    #input: a string
    #output: encoded data and its tree
    
    # convert the string into a list
    createnode(data)

    
    tree = huffman_tree()
    # sort data and make it into a tree
    
def createnode(data):
    #input: given data, usually a sentence
    #output: node objects used to build a tree
    data = list(data)
    letterlist = list()
    allnodes = list()
    for i in data:
        if i and i not in letterlist:
           
           letterlist.append(str(i))
           i = node_huffman(str(i))
           allnodes.append(i)
    return allnodes, letterlist
def huffman_decoding(data,tree):
    #output: decoded data
    pass
data = 'I am a big giant tree'
print(createnode(data))
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