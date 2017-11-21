# -*- coding:utf-8 -*-

from das.tree.merkle import Node
from das.tree.merkle import PrintVisitor
from hashlib import sha256
from collections import deque

HASHES = {key:sha256(bytes(str(key), 'utf-8')).hexdigest() for key in range(0, 100)}

def test_create_nodes():
    for key, value in HASHES.items():
        node = Node(data=key) 
        assert node
        assert node.hash == HASHES[key]

def test_add_lnode():
    pnode, lnode = Node(), Node(1)
    pnode.left = lnode

    phash = sha256(bytes(lnode.hash, 'utf-8')).hexdigest()
    assert pnode.hash == phash

def test_add_rnode():
    pnode, rnode = Node(), Node(1)
    pnode.right = rnode

    phash = sha256(bytes(rnode.hash, 'utf-8')).hexdigest()
    assert pnode.hash == phash
    
def test_create_tree1():
    pnode, lnode, rnode = Node(), Node(1), Node(2)
    pnode.left = lnode
    pnode.right = rnode

    phash = sha256(bytes(lnode.hash + rnode.hash, 'utf-8')).hexdigest()
    assert pnode.hash == phash
    return pnode

def test_create_tree2():
    nodes = deque([Node(data=key) for key in range(0, 4)])
    t = Node()
   
    while len(nodes):
        node = nodes.popleft()
        if t.left and t.right:
            nodes.append(t)
            t = Node()

        if not t.left:
            t.left = node
        elif not t.right:
            t.right = node
   
    return t

def test_apply_visitor():
    tree = test_create_tree2()
    pv = PrintVisitor()
    tree.accept(pv)

if __name__ == '__main__':
    tree = test_create_tree2()
    pv = PrintVisitor()
    tree.accept(pv)
    g = pv.graph
    g.format = 'png'
    g.render()
