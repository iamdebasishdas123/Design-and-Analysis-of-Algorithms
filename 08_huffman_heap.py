import heapq
from collections import Counter

class Node:
    def __init__(self, frequency, symbol, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def generate_codes(node, current_code, huffman_codes):
    if node is None:
        return
    
    if node.left is None and node.right is None:
        huffman_codes[node.symbol] = current_code
        return
   
    generate_codes(node.left, current_code + "0", huffman_codes)
    generate_codes(node.right, current_code + "1", huffman_codes)

def huffman_coding(data):
    frequency = Counter(data)

    heap = [Node(freq, symbol) for symbol, freq in frequency.items()]

    for item in heap:
        print(f"{item.symbol} : {item.frequency}\t")

    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(left.frequency + right.frequency, None, left, right)
        heapq.heappush(heap, merged)

    root = heap[0]
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    compressed_size = sum(len(huffman_codes[symbol]) * freq for symbol, freq in frequency.items())

    return huffman_codes, compressed_size

data = "BCCABBDDAECCBBAEDDCC"
print(f"Data:{data}")
codes, size = huffman_coding(data)
print(f"Huffman Codes: {codes}")
print(f"Size after Compression: {size} bits")