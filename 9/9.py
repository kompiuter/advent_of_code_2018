import re
from collections import defaultdict
from llist import dllist, dllistnode

n_players, n_marbles = list(map(int, re.findall(r'\d+', open('input.txt').read())))
scores = defaultdict(int)
lst = dllist([0, 1])
current_node = lst.nodeat(1)

for marble in range(2, n_marbles+1):
    if marble % 23 == 0:
        for i in range(7):
            current_node = current_node.prev if current_node.prev is not None else lst.last
        scores[marble % n_players] += marble + current_node.value  
        tmp_node = current_node
        current_node = current_node.next if current_node.next is not None else lst.first
        lst.remove(tmp_node)
    else:
        node = dllistnode(marble)
        if current_node.next == None:
            lst.insertnode(node, lst.nodeat(1))
        elif current_node.next.next == None:
            lst.appendnode(node)
        else:
            lst.insertnode(node, current_node.next.next)
        current_node = node

print(max(scores.values()))
