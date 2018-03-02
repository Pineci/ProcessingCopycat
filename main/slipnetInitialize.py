from slipnet import slipnet, node, link

s = slipnet()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetDepth = 10
numbers = ['one', 'two', 'three', 'four', 'five']
numbersDepth = 30

categories = [('letter-category', 30),
              ('length', 60),
              ('alphabetic-position', 80),
              ('string-position', 70),
              ('object-category', 90),
              ('bond-category', 80),
              ('group-category', 80)]

otherNodes = [('first', 60),
              ('last', 60),
              ('leftmost', 40),
              ('rightmost', 40),
              ('left', 40),
              ('right', 40),
              ('direction', 70),
              ('middle', 40),
              ('whole', 40),
              ('single', 40),
              ('letter', 20),
              ('group', 80),
              ('sameness', 80),
              ('predecessor-group', 50),
              ('successor-group', 50),
              ('sameness-group', 80)]

intrinsicNodes = [('identity', 90),
                  ('opposite', 90),
                  ('predecessor', 50),
                  ('successor', 50)]

s.addNodesConstantDepth(alphabet, alphabetDepth)
s.addNodesConstantDepth(numbers, numbersDepth)
s.addNodePairs(categories)
s.addNodePairs(otherNodes)
s.addNodePairs(intrinsicNodes)