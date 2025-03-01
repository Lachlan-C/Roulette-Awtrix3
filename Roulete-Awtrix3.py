IP = "0.0.0.0"

RED = "#FF0000"
BLACK = "#242124"
GREEN = "#008000"

WIDTH = 6
HEIGHT = 6

COUNT = 0
TIME = 10

APPNAME="Roulette"
URL = "/api/custom"
HEADER="?name="

import requests
import time
import random

def colour(num):
    if num == 0:
        return GREEN
    elif num % 2 == 0:
        return BLACK
    else:
        return RED

def draw(num):
    myobj = {"draw":[
    {"df": [-1 - (num % 7), 1, 6, 6, colour((((num // 7) - 2 ) % 15))]},
    {"df": [6 - (num % 7), 1, 6, 6, colour((((num // 7) - 1) % 15))]},
    {"df": [13 - (num % 7), 1, 6, 6, colour(((num // 7) % 15))]},
    {"df": [20 - (num % 7), 1, 6, 6, colour((((num // 7) + 1) % 15))]},
    {"df": [27 - (num % 7), 1, 6, 6, colour((((num // 7) + 2) % 15) )]},
    {"df": [34 - (num % 7), 1, 6, 6, colour((((num // 7) + 3) % 15))]}
    ]}  
    requests.post("http://"+IP+URL+HEADER+APPNAME, json = myobj)

def start(startNum,Target,StartTime):
    currentTime = StartTime
    VEL = 2*((Target-startNum)/TIME)
    ACCEL = -2*((Target-startNum)/TIME**2)
    COUNT = startNum
    while currentTime - StartTime < TIME:
        draw(int(COUNT))
        currentTime = time.time()
        timesec =  currentTime - StartTime
        COUNT = (VEL*timesec)+(0.5*ACCEL*(timesec**2))+startNum
    draw(Target)
    return ((Target // 7) % 15)

draw(0)
while True: 
    input("PRESS ENTER TO SPIN")
    rand = random.randint(1, 15)
    print(rand)
    output = start(COUNT*7,(15*7*5)+(rand*7),time.time())
    COUNT = output