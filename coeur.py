import math
from turtle import *

def dessina(k):
    return 15*math.sin(k)**3

def dessinb(k):
    return 12*math.cos(k)-5*\
            math.cos(2*k)-2*\
            math.cos(3*k)-\
            math.cos(4*k)


bgcolor("black")
for i in range(200):
    goto(dessina(i)*20 , dessinb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()
