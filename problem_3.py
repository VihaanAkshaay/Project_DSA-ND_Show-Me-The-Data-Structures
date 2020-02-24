import sys
import time

class Node:
    def __init__(self, freq, char = None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __str__(self):
        return "(char: {},count = {})".format(self.char, self.count)

def huffman_encoding(data):

    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char,0) +1
    if len(frequency)<2:
        if data == "":
            return "0", Node(1,"")
        else:
            return encode(data,generate_huffman_code(Node(1,data[0]))), Node(1,data[0])

     #To make nodes with frequency of the letter and the letter itself

    nodes = {}
    for char in frequency:
        nodes[char] = Node(frequency[char],char)

    #Now, generating trees,

    priority = 1
    node_0 = None
    node_1 = None
    parent_node = None

    while len(nodes)>1:
        change_priority = True
        min_priority = None
        for char in nodes:
            if nodes[char].freq == priority:
                if not node_0:
                    node_0 = nodes[char]
                elif not node_1:
                    node_1 = nodes[char]
            elif not min_priority or nodes[char].freq<min_priority:
                min_priority = nodes[char].freq

            if node_0 and node_1:
                parent_node = Node(node_0.freq + node_1.freq, node_0.char + node_1.char)
                parent_node.left = node_0
                parent_node.right = node_1
                nodes[parent_node.char] = parent_node
                nodes.pop(node_0.char)
                nodes.pop(node_1.char)
                node_0 = None
                node_1 = None
                change_priority = False
                break

        if change_priority:
            priority = min_priority
    tree = parent_node

    #to generate encoding
    encoding = generate_huffman_code(tree)
    encoded_data = encode(data,encoding)
    return encoded_data,tree

def generate_huffman_code(node, code = ""):
    encoding = {}
    if node:
        if not (node.left or node.right):
            if code =="":  #where only one letter is present
                encoding.update({node.char: "0"})
            else:
                encoding.update({node.char: code})
        encoding.update(generate_huffman_code(node.left,code + "0"))
        encoding.update(generate_huffman_code(node.right,code + "1"))
    return encoding

def encode(data,encoding):
    encoded_data = data
    for char in encoding:
        encoded_data = encoded_data.replace(char, encoding[char])
    return encoded_data

def huffman_decoding(data,tree):

    encoding = generate_huffman_reverse_code(tree)
    decoded_message = ""
    code = ""
    for ch in data:
        code += ch
        if code in encoding:
            decoded_message += encoding[code]
            code = ""

        return decoded_message
def generate_huffman_reverse_code(node , code = ""):
    encoding = {}
    if node:
        if not (node.left or node.right):
            if code == "": #Case of having only one letter
                encoding.update({"0:node.char})"})
            else:
                encoding.update({code: node.char})
        encoding.update(generate_huffman_reverse_code(node.left,code + "0"))
        encoding.update(generate_huffman_reverse_code(node.left, code+ "1"))
    return encoding

    pass

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
