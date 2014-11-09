__author__ = 'roohy'

from SearchFunctions import *


class Game:
    def __init__(self):
        self.root = ''
        self.target = ''
        self.states = None
        self.Mode = 0
    def setFunction(self):
        self.searchFunction = BFSSort if self.Mode == 1 else DFSSort if self.Mode == 2 else UFCSort
    def getRootNode(self):
        for state in self.states:
            if self.root == state.name:
                result = Node
                result.state = state
                result.cost = 0
                result.depth = 0
                result.parent = None
                return result
    def Search(self):
        self.setFunction()
        #print("starting search")
        result = Find(self.getRootNode(),self.target,self.searchFunction)
        temp = result[0]
        cost = temp.cost
        #print ('cost is ',cost)
        if result == None:
            return ['NoPathAvailable','','']
        pathSt = ""
        path = []
        result2 = []
        expanded = ""
        for n in result[1]:
            expanded = expanded + '-' + n.name
        expanded = expanded[1::]
        #print ('expand ',expanded)
        while temp != None:
            path.append(temp.state.name)
            #print('1', temp.state.name)
            temp = temp.parent
        path.reverse()
        for n in path:
            pathSt = pathSt + '-' + n
        pathSt = pathSt[1::]
        #print('pathst',pathSt)
        result2.append(expanded)
        result2.append(pathSt)
        result2.append(cost)
        return result2
