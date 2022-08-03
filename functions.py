from pyray import *
import math
import random
from inputs import *
from outputs import *

inputs = [ locX, locY, adjN, adjE, adjS, adjW, rdm, age, osc2, osc5, osc10] #11
outputs = [ moveN, moveE, moveS, moveW, moveR]#5

class Bug:
    def __init__(self, code, style):
        self.code = code
        self.style = style
        self.forward = 0

def generationGenerator( parents, count, w, h, complexity, mutation):
    #making an empty 2D list
    children = []
    for x in range(w):
        children.append([])
        for y in range(h):
            children[int(x)].append(None)
    #filling it with children
    validated = 0
    while validated < count:
        #finding a position
        x = random.randint( 0, w-1)
        y = random.randint( 0, h-1)
        while children[x][y] != None:
            x = random.randint( 0, w-1)
            y = random.randint( 0, h-1)
        #mixing two parents
        parent1 = parents[random.randint( 0, len(parents)-1)]
        parent2 = parents[random.randint( 0, len(parents)-1)]
        code = []
        style = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255]
        for synaps in range(complexity): #this is still random and does not take parents into consideration
            code.append([random.randint( 0, len(inputs)-1), #input
            random.random()*10-5, #weight
            random.randint( 0, len(outputs)-1)]) # output
        #mutating the code
        #appending the new born
        validated += 1
        children[x][y] = Bug( code, style)
    return children

def update(bugs, w, h, step, maxSteps):
    for x in range(w):
        for y in range(h):
            if bugs[x][y] != None:
                for connection in bugs[x][y].code:
                    if inputs[int(connection[0])](bugs, x, y, w, h, step, maxSteps) * connection[1] > 0.5:
                        outputs[connection[2]](bugs, x, y, w, h)
    return bugs

def render(bugs, res):
    begin_drawing()
    clear_background(Color( 30, 30, 50, 255))
    for x in range(len(bugs)):
        for y in range(len(bugs[x])):
            if bugs[x][y] != None:
                draw_circle( x*res + int(res/2), y*res + int(res/2), res/2, Color( bugs[x][y].style[0], bugs[x][y].style[1], bugs[x][y].style[2], 255))
    draw_fps( 5, 5)
    end_drawing()