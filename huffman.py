import heapq
from collections import Counter, namedtuple

# Node definition
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return (self.char or "") < (other.char or "")

# Build Huffman tree
def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(ch, f, None, None) for ch, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, new_node)
    return heap[0]

# Get Huffman codes
def get_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node.char:
        code_map[node.char] = prefix or "0"
    else:
        get_codes(node.left, prefix + "0", code_map)
        get_codes(node.right, prefix + "1", code_map)
    return code_map

# Collect all characters in a subtree
def get_all_chars(node):
    if node is None:
        return []
    if node.char:
        return [node.char]
    return get_all_chars(node.left) + get_all_chars(node.right)

# Label helper
def node_label(node):
    if node.char:
        return f"{node.char}({node.freq})"
    else:
        chars = "".join(sorted(get_all_chars(node)))
        return f"[{chars}:{node.freq}]"

# Build level-wise representation of the tree
def get_levels(root):
    levels = []
    this_level = [root]
    while any(this_level):
        levels.append(this_level)
        next_level = []
        for node in this_level:
            if node:
                next_level.append(node.left)
                next_level.append(node.right)
            else:
                next_level.extend([None, None])
        this_level = next_level
    return levels

# Pretty print the Huffman tree (centered layout)
def print_tree(root):
    levels = get_levels(root)
    max_width = 80
    per_level = max_width
    for i, level in enumerate(levels):
        line = ""
        per_level = max_width // (2 ** i)
        for node in level:
            if node:
                label = node_label(node)
            else:
                label = " "
            line += label.center(per_level)
        print(line.rstrip())
        if i < len(levels) - 1:
            print("")

# Encode the message
def huffman_encode(text, codes):
    return ''.join(codes[ch] for ch in text)

# Example usage
text = "PHOTOSYNTHESIS"

tree = build_huffman_tree(text)
codes = get_codes(tree)
encoded = huffman_encode(text, codes)

print("Frequencies:", dict(Counter(text)))
print("\nHuffman Tree (Centered Layout):")
print_tree(tree)

print("\nHuffman Codes:", codes)
print("Encoded Message:", encoded)
print("Original length (ASCII 8-bit):", len(text) * 8)
print("Encoded length (Huffman bits):", len(encoded))
print("Space saved (bits):", len(text) * 8 - len(encoded))
print("Space saved (%): {:.2f}%".format(100 * (len(text)*8 - len(encoded)) / (len(text)*8)))
