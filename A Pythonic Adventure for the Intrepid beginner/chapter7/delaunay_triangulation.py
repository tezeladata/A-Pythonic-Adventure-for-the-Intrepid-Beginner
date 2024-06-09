# We’re ready for the first major algorithm of this chapter. It
# takes a set of points as its input and returns a set of triangles as
# its output

# If we want to triangulate
# three points, there’s only one possible way to do so: output a
# triangle consisting of exactly those three points. If we want to
# triangulate more than three points, there will inevitably be
# more than one way to triangulate.

# We can accomplish triangulation manually by getting pen and
# paper and connecting dots. Unsurprisingly, we can do it better
# and faster by using an algorithm.

# What we’ll cover here is called the
# Bowyer-Watson algorithm, and it’s designed to take a set of
# points as its input and output a Delaunay triangulation.

# A Delaunay triangulation (DT) aims to avoid narrow, sliver
# triangles. It tends to output triangles that are somewhere close
# to equilateral.


# for a set of points, it is the set of
# triangles connecting all the points in which no point is inside
# the circumcircle of any of the triangles.


# Our eventual goal is to write a function that will take any set of
# points and output a full Delaunay triangulation. But let’s start
# with something simple: we’ll write a function that takes an
# existing DT of n points and also one point that we want to add
# to it, and outputs a DT of n + 1 points. This “Delaunay
# expanding” function will get us very close to being able to write
# a full DT function.


# A DT has only one rule: no point can lie within a circumcircle of
# any of its triangles. So we check the circumcircle of every circle
# in our existing DT, to determine whether point 10 lies within
# any of them. We find that point 10 lies within the circumcircles
# of three triangles

# Unfortunately, as is often the case with
# geometric algorithms, what seems clear and intuitive to the
# human eye can be tricky to write code for.



# Let's start with simple triangle:
# delaunay = [points_to_triangle((0.2,0.8),(0.5,0.2),(0.8,0.7))]

# Next, we want to add point in this triangle:
# point_to_add = [0.5,0.5]


# We first need to determine which, if any, triangles in the
# existing DT are now invalid because their circumcircle contains
# the point_to_add. For that, we do following:

# 1. Use a loop to iterate over every triangle in the existing DT.
# 2. For each triangle, find the circumcenter and radius of its circumcircle.
# 3. Find the distance between the point_to_add and this circumcenter.
# 4. If this distance is less than the circumradius, then the
# new point is inside the triangle’s circumcircle. We can
# then conclude this triangle is invalid and needs to be
# removed from the DT.

# invalid_triangles = []
# delaunay_index = 0

# while delaunay_index < len(delaunay):
#     circumcenter,radius = triangle_to_circumcenter(delaunay[delaunay_index])
#     new_distance = get_distance(circumcenter,point_to_add)

#     if(new_distance < radius):
#         invalid_triangles.append(delaunay[delaunay_index])
#     delaunay_index += 1


# Now we have a list of invalid triangles. Since they are invalid,
# we want to remove them. Eventually, we’ll also need to add new
# triangles to our DT. To do that, it will help to have a list of
# every point that is in one of the invalid triangles, as those
# points will be in our new, valid triangles.


# points_in_invalid = []
# for i in range(len(invalid_triangles)):
#     delaunay.remove(invalid_triangles[i])
#     for j in range(0,len(invalid_triangles[i])):
#         points_in_invalid.append(invalid_triangles[i][j])

# points_in_invalid = [list(x) for x in set(tuple(x) for x in points_in_invalid)]
# print(points_in_invalid, delaunay)


# The final step in our algorithm is the trickiest one. We have to
# add new triangles to replace the invalid ones. Each new triangle
# will have the point_to_add as one of its points, and and two
# points from the existing DT as its other points. However, we
# can’t add every possible combination of point_to_add and two
# existing points.






# for i in range(len(points_in_invalid)):
#     for j in range(i + 1,len(points_in_invalid)):
#         #count the number of times both of these are in the bad triangles
#         count_occurrences = 0
#         for k in range(len(invalid_triangles)):
#             count_occurrences += 1 * (points_in_invalid[i] in invalid_triangles[k]) *  (points_in_invalid[j] in invalid_triangles[k])
            
#             if(count_occurrences == 1):
#                 delaunay.append(points_to_triangle(points_in_invalid[i], points_in_invalid[j], point_to_add))

# print(delaunay)

# Here we loop through every point in points_in_invalid. For
# each one, we loop through every following point in
# points_in_invalid. This double loop enables us to consider
# every combination of two points that was in an invalid triangle.
# For each combination, we loop through all the invalid triangles
# and count how many times those two points are together in an
# invalid triangle. If they are together in exactly one invalid
# triangle, then we conclude that they should be together in one
# of our new triangles, and we add a new triangle to our DT that
# consists of those two points together with our new point.


# We have completed the steps that are required to add a new
# point to an existing DT. So we can take a DT that has n points,
# add a new point, and end up with a DT that has n + 1 points.



# we can combine the code we wrote earlier to
# create a function called gen_delaunay(), which takes a set of
# points as its input and outputs a full DT.



# The full DT generation function starts by adding the new
# outside triangle mentioned earlier. It then loops through every
# point in our collection of points 1. For every point, it creates a
# list of invalid triangles: every triangle that’s in the DT whose
# circumcircle includes the point we’re currently looking at 2.


import math
import numpy as np
import matplotlib.pyplot as plt

# Some function we will need later:
def points_to_triangle(point1, point2, point3):
    triangle = [list(point1), list(point2), list(point3)]
    return triangle

def triangle_to_circumcenter(triangle):
    x, y, z = complex(triangle[0][0], triangle[0][1]), complex(triangle[1][0], triangle[1][1]), complex(triangle[2][0], triangle[2][1])
    w = z - x
    w /= y - x
    c = (x-y) * (w-abs(w)**2) / 2j / w.imag - x
    radius = abs(c + x)
    return ((0 - c.real, 0 - c.imag), radius)

def get_distance(point1, point2):
    distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return distance



def gen_delaunay(points):
    delaunay = [points_to_triangle([-5, -5], [-5, 10], [10, -5])]
    number_of_points = 0
    
    # part1
    while number_of_points < len(points): 
        point_to_add = points[number_of_points]
        delaunay_index = 0

        # part2
        invalid_triangles = [] 
        while delaunay_index < len(delaunay):
            circumcenter, radius = triangle_to_circumcenter(delaunay[delaunay_index])
            new_distance = get_distance(circumcenter, point_to_add)

            if new_distance < radius:
                invalid_triangles.append(delaunay[delaunay_index])
            delaunay_index += 1

        # part3
        points_in_invalid = [] 
        for i in range(0, len(invalid_triangles)):
            delaunay.remove(invalid_triangles[i])
            for j in range(0, len(invalid_triangles[i])):
                points_in_invalid.append(invalid_triangles[i][j])

        points_in_invalid = [list(x) for x in set(tuple(x) for x in points_in_invalid)]

        # part4
        for i in range(0, len(points_in_invalid)): 
            for j in range(i + 1, len(points_in_invalid)):
                # count the number of times both of these are in the bad triangles
                count_occurrences = 0
                for k in range(0, len(invalid_triangles)):
                    count_occurrences += 1 * (points_in_invalid[i] in invalid_triangles[k]) * (points_in_invalid[j] in invalid_triangles[k])
                
                if count_occurrences == 1:
                    delaunay.append(points_to_triangle(points_in_invalid[i], points_in_invalid[j], point_to_add))
        
        number_of_points += 1

    return delaunay

N = 10
np.random.seed(5201314)
xs = np.random.rand(N)
ys = np.random.rand(N)
points = zip(xs, ys)
listpoints = list(points)
the_delaunay = gen_delaunay(listpoints)

# Visualize the result
plt.figure(figsize=(8, 8))
for triangle in the_delaunay:
    triangle.append(triangle[0])  # To close the triangle
    t = np.array(triangle)
    plt.plot(t[:, 0], t[:, 1], 'b-')

# Plot the points
plt.plot(xs, ys, 'ro')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Delaunay Triangulation')
plt.show()