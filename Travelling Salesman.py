import numpy as np
from matplotlib import pyplot as plt
import math

cities = np.loadtxt("cities")       #each line of the input text is x y of a city
l = len(cities)      
track = np.arange(l)                #names of the cities


def randomStart(seed=111):
    global cities, track
    np.random.seed(seed)
    np.random.shuffle(track)
    np.random.seed(seed)
    np.random.shuffle(cities)

def distance(a,b):
    return np.linalg.norm(a-b)

def lengthTotal():
    global cities,l
    tempL = 0
    for i in range(l):
        if i+1 < l:
           #tempL += math.sqrt(np.sum((cities[i]-cities[i+1])**2))
            tempL += distance(cities[i],cities[i+1])
    return tempL

def lengthChange(a1,a2,route):
    global l
    "New distances for new a1 city"
    tempL += distance(route[a1], route[min(a1-1, 0)])  #new left neighbor
    tempL -= distance(route[a2], route[min(a1-1, 0)])  #old left neighbor
    tempL += distance(route[a1], route[max(a1+1, l)])  #new right neighbor
    tempL -= distance(route[a2], route[max(a1+1, l)])  #old right neighbor
    "New distances for new a2 city"
    tempL += distance(route[a2], route[min(a2-1, 0)])  #new left neighbor
    tempL -= distance(route[a1], route[min(a2-1, 0)])  #old left neighbor
    tempL += distance(route[a2], route[min(a2+1, l)])  #new right neighbor
    tempL -= distance(route[a1], route[min(a2+1, l)])  #old right neighbor    
    return tempL    

def move():
    global track, cities, l, lengthCurrent
    a = np.random.randint(0,l, size = (1,2))
    a = a[0]
    a1 = a[0]
    a2 = a[1]
    tempCities = np.copy(cities)
    tempC = tempCities[a1]
    tempCities[a1] = tempCities[a2]
    tempCities[a2] = tempC
    change = lengthChange(a1,a2,tempCities)
    choice = np.random.rand()    
    if choic < math.exp(-change/temperature)   
    
randomStart()
lengthCurrent = lengthTotal()