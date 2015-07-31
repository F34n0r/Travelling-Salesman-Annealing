import numpy as np

n = 30          #number of cities
l = 100         #size of the largest square containing all the cities
cities = l*np.random.random_sample((n,2))
np.savetxt("input",cities)