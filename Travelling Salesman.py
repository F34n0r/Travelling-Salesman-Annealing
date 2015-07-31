import numpy as np
from matplotlib import pyplot as plt
import math

cities = np.loadtxt("input")       #each line of the input text is x y of a city
l = len(cities)      
track = np.arange(l)                #names of the cities
startTemperature = 2.
stepsPerTemp = 10000
temperatureSteps = 100

"The total number of steps is: stepsPerTemp * temperatureSteps"

distanceList = list()

def decreaseTemperatureLin():
    global temperature
    temperature -= startTemperature/temperatureSteps

def decreaseTemperatureExp(t):
    global temperature
    temperature = startTemperature*math.exp(-t)

def randomStart(seed=111):
    global cities, track
    np.random.seed(seed)
    np.random.shuffle(track)
    np.random.seed(seed)
    np.random.shuffle(cities)

def distance(a,b):
    #print np.linalg.norm(a-b), a, b
    return np.linalg.norm(a-b)


def lengthTotal(cities):
    global l,distanceListReal
    distanceListReal = list()
    for i in range(l-1):
        distanceListReal.append(distance(cities[i],cities[i+1]))
    d = np.array(distanceListReal)
    return np.sum(d)

def lengthChange(a1,a2,route):
    global l,cities
    tempL = 0
    #print a1, a2
    city1 = route[a1]
    city2 = route[a2]
   
    oldLeft1 = distance(city2,cities[max(a1-1,0)])
    oldRight1 = distance(city2, cities[min(a1+1,l-1)])
    oldLeft2 = distance(city1, cities[max(a2-1,0)])
    oldRight2 = distance(city1, cities[min(a2+1,l-1)])
    
    newLeft1 = distance(city1,route[max(a1-1,0)])
    newRight1 = distance(city1, route[min(a1+1,l-1)])
    newLeft2 = distance(city2, route[max(a2-1,0)])
    newRight2 = distance(city2, route[min(a2+1,l-1)])

    old = oldLeft1 + oldLeft2 + oldRight1 + oldRight2
    new = newLeft1 + newLeft2 + newRight1 + newRight2
    tempL = new - old
    #print "Change: " + str(tempL)    
    return tempL    

def move():
    global track, cities, l, lengthCurrent,wrong
    a = np.random.randint(0,l, size = (1,2))
    a = a[0]
    a1 = a[0]
    a2 = a[1]
    tempCities = np.copy(cities)
    tempCities[a1] , tempCities[a2] = np.copy(tempCities[a2]), np.copy(tempCities[a1])
    change = lengthChange(a1,a2,tempCities)
    #change = lengthTotal(tempCities) - lengthTotal(cities)
    if change < 0:
        cities[a1], cities[a2] = np.copy(cities[a2]), np.copy(cities[a1])
        track[a1], track[a2] = track[a2], track[a1]
        lengthCurrent += change
    else:        
        choice = np.random.rand()
        #print a1,a2
        #print change
        if choice < math.exp(-change/temperature):
            cities[a1], cities[a2] = np.copy(cities[a2]), np.copy(cities[a1])
            track[a1], track[a2] = track[a2], track[a1]
            lengthCurrent += change
        #else:
            #print "Nope"

temperature = startTemperature  
randomStart(np.random.randint(100000))
lengthCurrent = lengthTotal(cities)
for j in range(temperatureSteps):
    for i in range(stepsPerTemp):
        move()
        distanceList.append(lengthCurrent)
        #print "  Additive          Real"
        print lengthCurrent #, lengthTotal(cities)
    decreaseTemperatureLin()
    
plt.plot(distanceList)
plt.show()