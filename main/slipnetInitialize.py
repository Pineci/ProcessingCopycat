from slipnet import slipnet, node, link

s = slipnet()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetDepth = 10
numbers = ['one', 'two', 'three', 'four', 'five']
numbersDepth = 30

categories = [('letter-category', 30)
              ('length', 60)
              ('alphabetic-position', 80)
              ('string-position', 70)
              ('object-category', 90)
              ('bond-category', 80)
              ('group-category', 80)]

s.addNodesConstantDepth(alphabet, alphabetDepth)
s.addNodesConstantDepth(numbers, numbersDepth)
s.addNodePairs(categories)