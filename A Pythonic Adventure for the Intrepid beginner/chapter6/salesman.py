# We say that salesman has to visit 40 cities - N = 40
# x and y are coordinates of out cities

import numpy as np
random_seed = 1729
np.random.seed(random_seed)
N = 40
x = np.random.rand(N)
y = np.random.rand(N)

# In this snippet, we used the numpy module’s random.seed()
# method. This method takes any number you pass to it and uses
# that number as a “seed” for its pseudorandom number
# generation algorithm

# Next, we’ll zip the x values and y values together to create
# cities, a list containing the coordinate pair for each of our 40
# randomly generated city locations.
points = zip(x, y)
cities = list(points)
print(cities)

# We can refer to the first city as cities[0], the
# second as cities[1], and so on.


# Our first proposed solution will be to simply visit all
# the cities in the order in which they appear in the cities list.
# We can define an itinerary variable that will store this order in
# a list:

itinerary = list(range(0, N))
# The order of the numbers in our itinerary is the order in which
# we’re proposing to visit our cities: first city 0, then city 1, and so
# on.


# let’s say it
# costs one dollar to travel a distance of 1, no matter which
# direction and no matter which cities we’re traveling between.

# In this case, minimizing the cost is
# the same as minimizing the distance traveled.



# To determine the distance required by a particular itinerary, we
# need to define two new functions. First, we need a function that
# will generate a collection of lines that connect all of our points.

# lines = []
# Next, we can iterate over every city in our itinerary, at each step
# adding a new line to our lines collection that connects the
# current city and the city after it.
# for j in range(0,len(itinerary) - 1):
#     lines.append([cities[itinerary[j]],cities[itinerary[j + 1]]])



# We can put these elements together in one function called
# genlines (short for “generate lines”), which takes cities and
# itinerary as arguments and returns a collection of lines
# connecting each city in our list of cities, in the order specified
# in the itinerary:
def genlines(cities,itinerary):
    lines = []
    for j in range(0,len(itinerary) - 1):
        lines.append([cities[itinerary[j]],cities[itinerary[j + 1]]])

    return lines


# This function takes a list of lines as its input and outputs the
# sum of the lengths of every line.
import math
def howfar(lines):
    distance = 0
    for j in range(len(lines)):
        distance += math.sqrt((lines[j][1][0] - lines[j][0][0])**2 + (lines[j][1][1] - lines[j][0][1])**2)
    return distance

totaldistance = howfar(genlines(cities,itinerary))
print(totaldistance)



import matplotlib.collections as mc
import matplotlib.pylab as pl
def plotitinerary(cities,itin,plottitle,thename):
    lc = mc.LineCollection(genlines(cities,itin), linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.scatter(x, y)
    pl.title(plottitle)
    pl.xlabel('X Coordinate')
    pl.ylabel('Y Coordinate')
    pl.savefig(str(thename) + '.png')
    pl.close()

plotitinerary(cities,itinerary,'TSP - Random Itinerary','figure2')