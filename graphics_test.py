import os
import turtle
import time

def startUp():
    os.environ['DISPLAY'] = ':0'
    
def TurtleTest():
    t = turtle.Turtle()
    t.forward(100)
    t.left(90)
    t.forward(100)
    time.sleep(5)
    quit()

if __name__ == '__main__':
    startUp()
    TurtleTest()