
class slipnet:
    
    def __init__(self):
        self.nodes = {}
        self.numNodes = 0
        
    def addNode(self, node):
        self.nodes[node.getName()] = node
        self.numNodes = self.numNodes + 1
        
    def addNodes(self, nameArr, depthArr):
        for i in range(len(nameArr)):
            self.addNode(node(nameArr[i], depthArr[i]))
            
    def addNodesConstantDepth(self, nameArr, depth):
        for i in range(len(nameArr)):
            self.addNode(node(nameArr[i]), depth)
            
    def addNodePair(self, pair):
        name, depth = pair
        self.addNode(node(name, depth))
        
    def addNodePairs(self, pairs):
        for i in range(len(pairs)):
            self.addNodePair(pairs[i])
        
    def getNode(self, nodeName):
        if nodeName in self.nodes:
            return self.nodes[nodeName]
        else:
            return None
        
    def addLink(self, frmName, toName, link):
        self.nodes[frmName].addConnection(toName, link)
            
    def getLink(self, frmName, toName):
        return self.nodes[frmName].getLink(toName)
    
    def getLinkFrom(self, frmName):
        return self.nodes[frmName].getLinksFrom()
        
    def getLinkTo(self, toName):
        links = {}
        for key in self.nodes:
            linksFrom = self.nodes[key].getLinksFrom()
            if toName in linksFrom:
                links[key] = linksFrom[toName]
        return links
        
    def __repr__(self):
        for key in self.nodes:
            print(self.nodes[key])
           

class node:
    
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
        self.connected = {}
        self.activation = 0
        
    def addConnection(self, nodeName, link):
        self.connected[nodeName] = link
        
    def getConnections(self):
        return self.connected.keys()
    
    def getName(self):
        return self.name
    
    def getLinksFrom(self):
        return self.connected
    
    def getLink(self, nodeName):
        return self.connected[nodeName]
    
    def isActive(self):
        return 100 == self.activation
    
    def __repr__(self):
        return 'Node: Name={0}, Depth={1}, Activation={2}'.format(self.name, self.depth, self.activation)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        return False
        
class link:
    
    def __init__(self, type, intrinsic, length):
        self.type = type
        self.intrinsic = intrinsic
        self.length = length
        
    def __repr__(self):
        return 'Link: Type={0}, Intrinsic={1}, Length={2}'.format(self.type, self.intrinsic, self.length)