__author__ = 'roohy'



class Node:
    def __init__(self):
        self.parent = None
        self.state = None
        self.depth = 0
        self.cost = 0
class State:
    def __init__(self):
        self.name = ''
        self.number = 0
        self.connections = []

def Find(rootNode,destination , sortFunction):
    print("Find function")
    queue = [rootNode]
    explored = []
    while len(queue) > 0 :
        sortFunction(queue)
        tempNode = queue.pop()
        if tempNode.state in explored:
            continue
        print("examination of ",tempNode.state.name)
        if tempNode.state.name == destination:
            print('found eachother',tempNode.cost)
            return [tempNode,explored]
        for connection in tempNode.state.connections:
            print(tempNode.state.name,' is friends with',connection[0].name)
            if connection[0] not in explored:
                newNode = Node()
                newNode.parent = tempNode
                newNode.state = connection[0]
                newNode.cost = connection[1] + tempNode.cost
                newNode.depth = tempNode.depth + 1
                queue.append(newNode)
        explored.append(tempNode.state)
        print('rr', [ex.name for ex in explored])
    return None

def BFSSort(nodes):
    nodes.sort(key = lambda node: (node.depth,node.state.name) )
    nodes.reverse()
    for node in nodes:
        print ('nn',node.depth,node.state.name)
def DFSSort(nodes):
    nodes.sort(key = lambda node: node.state.name)
    nodes.sort(key = lambda node: node.depth)
    nodes.reverse()
def UFCSort(nodes):
    nodes.sort(key = lambda node: (node.cost , node.state.name) )
    nodes.reverse()