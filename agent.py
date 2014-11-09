from FileOperation import WriteFile

__author__ = 'roohy'

import sys
import FileOperation
from GameClass import Game

#print('Program starting')
#print('reading from ',sys.argv[1])
game = FileOperation.FileRead('input.txt')
result = game.Search()
WriteFile('output.txt',result[0],result[1],str(result[2]))
