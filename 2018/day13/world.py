import numpy as np
import re

dirList = {'>':(1,0),'v':(0,1),'<':(-1,0),'^':(0,-1)}

class tracks:
    def __init__(self):
        self.space = [list(line.strip('\n')) for line in open('./2018/day13/input.txt', 'r').readlines()]

class car:
    
    def __init__(self, x, y, facing):
        self.pos = np.array((x,y))
        self.dir = np.array(dirList[facing])
        self.nextTurn = 1
        self.crashed = False

    def turn(self, to, intersection):
        if to == 'L': # turn left
            mult = -1 if self.dir[1] == 0 else 1
            self.dir = np.array((self.dir[1], self.dir[0] * mult))
        elif to == 'R': # turn right
            mult = -1 if self.dir[0] == 0 else 1
            self.dir = np.array((self.dir[1] * mult, self.dir[0]))
        if intersection:
            self.nextTurn += 2 if self.nextTurn == -1 else - 1

    def move(self, track):
        self.pos += self.dir
        tile = track.space[self.pos[1]][self.pos[0]]
        if tile == '+': # turn according to the nextTurn
            self.turn('L' if self.nextTurn == 1 else 'R' if self.nextTurn == -1 else '', True)
        elif tile == '/': # if we move horizontaly, go left, else go right
            self.turn('L' if self.dir[1] == 0 else 'R', False) 
        elif tile == '\\': # if we move verticaly, go left, else go right
            self.turn('L' if self.dir[0] == 0 else 'R', False)
    
    def crash(self):
        self.crashed = True
        self.pos[0], self.pos[1] = -1, -1