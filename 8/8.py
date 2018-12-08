from collections import defaultdict
from operator import itemgetter
import itertools

num_list = list(map(int, open('input.txt').read().split()))

def _build_tree(tree, l, i, name_iter):
    node_name = next(name_iter)
    children, metadata = l[i], l[i+1]
    i += 2
    for _ in range(children):
        child, i = _build_tree(tree, l, i, name_iter)
        tree[node_name][0].append(child)
    for i in range(i, i + metadata):
        tree[node_name][1].append(l[i])
    return node_name, i+1

def build_tree(tree, l):
    _build_tree(tree, l, 0, itertools.count(0))

tree = defaultdict(lambda: ([], []))
build_tree(tree, num_list)
print('metadata sum:', sum([sum(metadata) for (_, (_, metadata)) in tree.items()]))   

node_values = defaultdict(int)
def get_value(node):
    if node in node_values:
        return node_values[node]
    
    children, metadata = tree[node]
    if not children:
        value = sum(metadata)
    else:
        value = 0
        for index in metadata:
            if index <= len(children):
                value += get_value(children[index-1])
    
    node_values[node] = value
    return value

print('root value:', get_value(0))