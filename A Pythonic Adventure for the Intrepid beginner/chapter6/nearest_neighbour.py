import math

# For cities:
import numpy as np
random_seed = 1729
np.random.seed(random_seed)
N = 40
x = np.random.rand(N)
y = np.random.rand(N)

points = zip(x, y)
cities = list(points)

# Next we’ll consider a simple, intuitive method called the
# nearest neighbor algorithm. We start with the first city on the
# list. Then we simply find the closest unvisited city to the first
# city and visit that city second. At every step, we simply look at
# where we are and choose the closest unvisited city as the next
# city on our itinerary. This minimizes the travel distance at each
# step, although it may not minimize the total travel distance

# Suppose that we have a point called
# point and a list of cities called cities. The distance between
# point and the jth element of cities is given by the following
# Pythagorean-style formula


point = [0.5,0.5]
j = 10
distance = math.sqrt((point[0] - cities[j][0])**2 + (point[1] -
cities[j][1])**2)
print(cities, distance)


# If we want to find which element of cities is closest to our
# point (the point’s nearest neighbor), we need to iterate over
# every element of cities and check the distance between the
# point and every city


def findnearest(cities,idx,nnitinerary):
    point = cities[idx]
    mindistance = float('inf')
    minidx = - 1
    for j in range(0,len(cities)):
        distance = math.sqrt((point[0] - cities[j][0])**2 + (point[1] - cities[j][1])**2)
        
        if distance < mindistance and distance > 0 and j not in nnitinerary:
            mindistance = distance
            minidx = j
    
    return minidx 


# After we have this findnearest() function, we’re ready to
# implement the nearest neighbor algorithm. Our goal is to
# create an itinerary called nnitinerary. We’ll start by saying that
# the first city in cities is where our salesman starts:
nnitinerary = [0]


# If our itinerary needs to have N cities, our goal is to iterate over
# all the numbers between 0 and N – 1, find for each of those
# numbers the nearest neighbor to the most recent city we
# visited, and append that city to our itinerary.
# We can accomplish following by creating function
# called donn - do nearest neighbour

# It starts with the first city in cities, and at
# every step adds the closest city to the most recently added city
# until every city has been added to the itinerary.

def donn(cities,N):
    nnitinerary = [0]
    for j in range(0,N - 1):
        next = findnearest(cities,nnitinerary[len(nnitinerary) - 1],nnitinerary)
        nnitinerary.append(next)
    
    return nnitinerary


def genlines(cities,itinerary):
    lines = []
    for j in range(0,len(itinerary) - 1):
        lines.append([cities[itinerary[j]],cities[itinerary[j + 1]]])

    return lines

def howfar(lines):
    distance = 0
    for j in range(len(lines)):
        distance += math.sqrt((lines[j][1][0] - lines[j][0][0])**2 + (lines[j][1][1] - lines[j][0][1])**2)
    return distance

print(howfar(genlines(cities,donn(cities,N))))


# page 236