from slipnet import slipnet, node, link

s = slipnet()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetDepth = 10
numbers = ['one', 'two', 'three', 'four', 'five']
numbersDepth = 30
categories = ['letter-category', 'length', 'alphabetic-position', 'string-position', 'object-category', 'bond-category', 'group-category']
categoriesDepth = [30, 60, 80, 70, 90, 80, 80]


for node in nodes:
    s.addNode(node)