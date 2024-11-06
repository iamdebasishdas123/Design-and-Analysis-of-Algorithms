from collections import Counter

class Node:
    def __init__(self, frequency, char, left=None, right=None):
        self.frequency = frequency  
        self.char = char 
        self.left = left  
        self.right = right 

    def __lt__(self, other):
        return self.frequency < other.frequency

def insert_into_queue(queue, node):
    queue.append(node)
    queue.sort(key=lambda x: x.frequency)

def generate_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.left is None and node.right is None:
        huffman_codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", huffman_codes)
    generate_codes(node.right, current_code + "1", huffman_codes)

def huffman_coding(data):
    frequency = Counter(data)

    priority_queue = [Node(freq, char) for char, freq in frequency.items()]
    
    priority_queue.sort(key=lambda x: x.frequency)

    for item in priority_queue:
        print(f"{item.char} : {item.frequency}\t")

    while len(priority_queue) > 1:
        left = priority_queue.pop(0) 
        right = priority_queue.pop(0) 

        merged = Node(left.frequency + right.frequency, None, left, right)

        insert_into_queue(priority_queue, merged)

    root = priority_queue[0]

    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    compressed_size = sum(len(huffman_codes[symbol]) * freq for symbol, freq in frequency.items())

    return huffman_codes, compressed_size

data = "BCCABBDDAECCBBAEDDCC"
print(f"Data:{data}")
huffman_codes, size = huffman_coding(data)
print(f"Huffman Codes: {huffman_codes}")
print(f"Compressed Size: {size} bits")