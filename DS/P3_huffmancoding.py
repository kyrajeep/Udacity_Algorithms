import sys
'''
 huffman tree:
1. nodes as weights. build a min heap. 
2. take out two smallest nodes
3. combine them to make an internal node.
'''
#a min heap is used as a priority queue to pop the 
#smallest node at the root
class node_huffman:
    # a class for nodes
    def __init__(self, letter):
        self.letter = letter   
        self.weight = 1
        self.left = None
        self.right = None
        
class huffman_tree:
    # note to self: Does it make sense to build this with a list?
    def __init__(self):
        self.root = None
        self.heap_l = []
    
    def insert(self, node):
        # the edges are represented as the children
        if self.root is None:
            self.root = node
                    
    def remove():
        self.heap_l.pop(index = 0)
        '''
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
def create_pqueue(data):
    #input: a string (data)
    #output: priority queue with nodes
    #convert the string into a list of nodes
    list_nodes = create_node(data)
    print(list_nodes)
    list_nodes = sorted(list_nodes.items(), key = lambda x: x[1])
        
    return list_nodes
def create_node(data):
    #input: given data, usually a sentence
    #output: node objects used to build a tree
    data = list(data)
    letterlist = []
    all_nodes = dict()
    for i in data:
        if i not in letterlist and i != ' ':
            letterlist.append(i)
            # i-th node is in the all_nodes list
            all_nodes[i] = 1
            
        elif i in letterlist:
            all_nodes[i] += 1
            
    return all_nodes

def huffman_encoding(data):
    list_nodes = create_tree(data)
    init_tree = list_nodes
    while len(list_nodes) >= 3:
        combined = ('combined', list_nodes[0][1] + list_nodes[1][1] )
        list_nodes.pop(0)
        list_nodes.pop(1)
        list_nodes.append(combined)
    last_combo = ('last_combo', list_nodes[0][1] + list_nodes[1][1] )
    list_nodes.append(last_combo)
    list_nodes.pop(0)
    list_nodes.pop(1)
    return list_nodes, init_tree
    
def huffman_decoding(data,tree):
    #output: decoded data
    pass

# test case 1
#data = 'I am a big giant tree'
#print(huffman_encoding(data))

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

 #   decoded_data = huffman_decoding(encoded_data, tree)

 #   print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
 #   print ("The content of the encoded data is: {}\n".format(decoded_data))



