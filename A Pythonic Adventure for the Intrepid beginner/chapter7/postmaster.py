import math

# By now,
# you won’t be surprised to learn that
# advanced geometry is a natural fit for
# algorithmic reasoning.

# after you make
# the assignments of which post office should deliver to which
# homes, the individual letter carriers can use the TSP to decide
# the order in which to visit those homes.

# The simplest approach to this problem, which we might call the
# postmaster problem, is to consider each house in turn,
# calculating the distance between the house and each of the four
# post offices, and assigning the closest post office to deliver to
# the house in question.

# There lies weakness of that whole algorithm:
# By calculating distances for each house individually, we’re
# repeating work that we wouldn’t have to do if we could
# somehow make generalizations about entire neighborhoods or
# regions.


# A more elegant approach would be to consider the map as a
# whole and separate it into distinct regions, each of which
# represents one post office’s assigned service area. By drawing
# just two straight lines, we can accomplish that with our
# hypothetical town

# Now that the
# entire map is subdivided, we can easily assign any new
# construction to its closest post office simply by checking which
# region it’s in.


# A diagram that subdivides a map into regions of closest
# proximity, as ours does, is called a Voronoi diagram. Voronoi
# diagrams have a long history going all the way back to René
# Descartes.

# This chapter will introduce an algorithm for
# generating a Voronoi diagram for any set of points, thereby
# solving the postmaster problem.



# Points are represented in x,y coordinates
point = [0.2,0.8]

# At the next level of complexity, we combine points to form
# triangles. We’ll represent a triangle as a list of three points:
triangle = [[0.2,0.8],[0.5,0.2],[0.8,0.7]]


# Triangle generator:
def points_to_triangle(point1,point2,point3):
    triangle = [list(point1),list(point2),list(point3)]
    return triangle


# Function to generate lines:
def genlines(listpoints,itinerary):
    lines = []

    for j in range(len(itinerary)-1):
        lines.append([listpoints[itinerary[j]],listpoints[itinerary[j+1]]])
    return lines

# Next, we’ll create our simple plotting function. It will take a
# triangle we pass to it, split it into its x and y values, call
# genlines() to create a collection of lines based on those values,
# plot the points and lines, and finally save the figure to a .png
# file.

import pylab as pl
from matplotlib import collections as mc

def plot_triangle_simple(triangle,thename):
    fig, ax = pl.subplots()

    xs = [triangle[0][0],triangle[1][0],triangle[2][0]]
    ys = [triangle[0][1],triangle[1][1],triangle[2][1]]

    itin=[0,1,2,0]

    thelines = genlines(triangle,itin)

    lc = mc.LineCollection(genlines(triangle,itin), linewidths=2)

    ax.add_collection(lc)

    ax.margins(0.1)
    pl.scatter(xs, ys)
    pl.savefig(str(thename) + '.png')
    pl.close()

plot_triangle_simple(points_to_triangle((0.2,0.8),(0.5,0.2),
(0.8,0.7)),'tri')



# We can also implement pythagorean theorem to calculate
# distance between any two objects
def get_distance(point1,point2):
    distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return distance


# All three lines
# will meet at a single point no matter what triangle you start
# with. The point where they meet is commonly called the
# centroid of the triangle, and it’s always on the inside in a place
# that looks like it could be called the triangle’s center.


# Here is another
# of the rich phenomena related to triangles: every triangle has
# one unique circle that goes through all three of its points. This
# circle is called the circumcircle because it is the circle that
# circumscribes the triangle.

# We can write a function that finds the circumcenter and
# circumradius (the radius of the circumcircle) for any given
# triangle. This function relies on conversion to complex
# numbers. It takes a triangle as its input and returns a center
# and a radius as its output:

def triangle_to_circumcenter(triangle):
    x,y,z = complex(triangle[0][0],triangle[0][1]), complex(triangle[1][0],triangle[1][1]), complex(triangle[2][0],triangle[2][1])
    w = z - x
    w /= y - x
    c = (x-y) * (w-abs(w)**2)/2j/w.imag - x
    radius = abs(c + x)
    return((0 - c.real,0 - c.imag),radius)

print(triangle_to_circumcenter([(0.2,0.8),(0.5,0.2), (0.8,0.7)]))


# We improved our function
def plot_triangle(triangles,centers,radii,thename):
    fig, ax = pl.subplots()
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    for i in range(0,len(triangles)):
        triangle = triangles[i]
        center = centers[i]
        radius = radii[i]
        itin = [0,1,2,0]
        thelines = genlines(triangle,itin)
        xs = [triangle[0][0],triangle[1][0],triangle[2][0]]
        ys = [triangle[0][1],triangle[1][1],triangle[2][1]]

        lc = mc.LineCollection(genlines(triangle,itin), linewidths = 2)

        ax.add_collection(lc)
        ax.margins(0.1)
        pl.scatter(xs, ys)
        pl.scatter(center[0],center[1])

        circle = pl.Circle(center, radius, color = 'b', fill = False)

        ax.add_artist(circle)

    pl.savefig(str(thename) + '.png')
    pl.close()


# Now we can plot two triangles
triangle1 = points_to_triangle((0.1,0.1),(0.3,0.6),(0.5,0.2))
center1,radius1 = triangle_to_circumcenter(triangle1)
triangle2 = points_to_triangle((0.8,0.1),(0.7,0.5),(0.8,0.9))
center2,radius2 = triangle_to_circumcenter(triangle2)
plot_triangle([triangle1,triangle2],[center1,center2],
[radius1,radius2],'two')
