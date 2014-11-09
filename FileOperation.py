__author__ = 'roohy'

from SearchFunctions import State
from GameClass import Game

def FileRead(addr):
    FILE = open(addr,'r')
    fileString = FILE.read()
    print("file being read")
    stringList = fileString.split('\n')
    states = []
    searchMode = int(stringList[0])
    print('search mode ', searchMode)
    print(stringList[1],' is looking for' , stringList[2])
    sourceName = stringList[1]
    targetName = stringList[2]
    stateCount = int(stringList[3])
    print('total number of states ',stateCount)
    for i in range(4,4+stateCount):
        temp = State()
        temp.name = stringList[i]
        states.append(temp)
    for i in range(0,stateCount):
        row = stringList[4+stateCount+i].split(' ')
        for j in range(0,stateCount):
            if int(row[j]) != 0:
                states[i].connections.append((states[j],int(row[j])))
                print(states[i].name , 'is friends with',states[j].name,"with the cost of",row[j])
    game = Game()
    game.states = states
    game.Mode = searchMode
    game.root = sourceName
    game.target = targetName
    return game

def WriteFile(filename , expand , path , cost):
    FILE = open(filename,'w')
    FILE.write(expand+'\n'+path+'\n'+cost)