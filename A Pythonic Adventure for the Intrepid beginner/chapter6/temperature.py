# To do worse with the intention of eventually doing better is a
# delicate undertaking

# We need to find a way to do worse
# only a little, only occasionally, and only in the context of
# learning how to eventually do better.

# If we consider the time 10 minutes
# before the end, we’ll have a more moderate version of the
# mindset we had 10 seconds before the end. Since the end is
# near, we’ll be motivated to go directly upward.

# Our
# temperature function is relatively simple. It takes t as an
# argument, where t stands for time:
temperature = lambda t: 1/(t + 1)

# we use 1 to represent
# our maximum temperature, 0 to represent our minimum
# temperature, 0 to represent our minimum time, and 99 to
# represent our maximum time, without specifying units.
import matplotlib.pyplot as plt
import math
import numpy as np

ts = list(range(0,100))
plt.plot(ts, [temperature(t) for t in ts])
plt.title('The Temperature Function')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.show()


# Let’s bring all of our ideas together: the temperature function,
# the search problem in hilly terrain, the perturb search
# algorithm, and the TSP. In the context of the TSP, the complex,
# hilly terrain that we’re in consists of every possible solution to
# the TSP.

# When we start, our high temperature will dictate
# more openness to choosing a worse itinerary

# The algorithm we’ll implement, simulated annealing, is a
# modified form of the perturb search algorithm. The essential
# difference is that in simulated annealing, we’re sometimes
# willing to accept itinerary changes that increase the distance
# traveled, because this enables us to avoid the problem of local
# optimization. Our willingness to accept worse itineraries
# depends on the current temperature.


# If the random number is lower
# than the temperature, then we’ll be willing to accept a worse
# itinerary. If the random number is higher than the
# temperature, then we won’t be willing to accept a worse
# itinerary.

# That way, we’ll have occasional, but not constant,
# times when we accept worse itineraries, and our likelihood of
# accepting a worse itinerary will decrease over time as our
# temperature cools

N = 40
x = np.random.rand(N)
y = np.random.rand(N)

points = zip(x, y)
cities = list(points)


def howfar(lines):
    distance = 0
    for j in range(len(lines)):
        distance += math.sqrt((lines[j][1][0] - lines[j][0][0])**2 + (lines[j][1][1] - lines[j][0][1])**2)
    return distance

def genlines(cities,itinerary):
    lines = []
    for j in range(0,len(itinerary) - 1):
        lines.append([cities[itinerary[j]],cities[itinerary[j + 1]]])

    return lines

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


def donn(cities,N):
    nnitinerary = [0]
    for j in range(0,N - 1):
        next = findnearest(cities,nnitinerary[len(nnitinerary) - 1],nnitinerary)
        nnitinerary.append(next)
    
    return nnitinerary


def perturb(cities,itinerary):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.floor(np.random.rand() * (len(itinerary)))

    itinerary2 = itinerary.copy()

    itinerary2[neighborids1] = itinerary[neighborids2]
    itinerary2[neighborids2] = itinerary[neighborids1]

    distance1 = howfar(genlines(cities,itinerary))
    distance2 = howfar(genlines(cities,itinerary2))

    itinerarytoreturn = itinerary.copy()

    if(distance1 > distance2):
        itinerarytoreturn = itinerary2.copy()

    return(itinerarytoreturn.copy())


def perturb_sa1(cities,itinerary,time):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.floor(np.random.rand() * (len(itinerary)))

    itinerary2 = itinerary.copy()

    itinerary2[neighborids1] = itinerary[neighborids2]
    itinerary2[neighborids2] = itinerary[neighborids1]

    distance1 = howfar(genlines(cities,itinerary))
    distance2 = howfar(genlines(cities,itinerary2))

    itinerarytoreturn = itinerary.copy()

    randomdraw = np.random.rand()
    temperature = 1/((time/1000) + 1)

    if((distance2 > distance1 and (randomdraw) < (temperature)) or
    (distance1 > distance2)):
        itinerarytoreturn=itinerary2.copy()

    return(itinerarytoreturn.copy())


# changed the temperature function a little; because we’ll be
# calling this function with very high time values, we use
# time/1000 instead of time as part of the denominator argument
# in our temperature function

itinerary = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25, 26,27,28,29, 30,31,32,33,34,35,36,37,38,39]

itinerary_ps = itinerary.copy()
for n in range(0,len(itinerary) * 500):
 itinerary_ps = perturb(cities,itinerary_ps)
print(howfar(genlines(cities,itinerary_ps)))

np.random.seed(1729)
itinerary_sa = itinerary.copy()
for n in range(0,len(itinerary) * 50000):
 itinerary_sa = perturb_sa1(cities,itinerary_sa,n)
print(howfar(genlines(cities,itinerary))) #random itinerary
print(howfar(genlines(cities,itinerary_ps))) #perturb search
print(howfar(genlines(cities,itinerary_sa))) #simulated annealing
print(howfar(genlines(cities,donn(cities,N)))) #nearest neighbor