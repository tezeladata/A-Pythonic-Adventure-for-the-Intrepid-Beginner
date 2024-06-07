# It might occur to you to make a list of every possible itinerary
# that can connect our cities and evaluate them one by one to see
# which is best. If we want to visit three cities, the following is an
# exhaustive list of every order in which they can be visited:
visited = [[1, 2, 3], [1, 3, 2], [2, 3, 1], [2, 1, 3], [3, 1, 2], [3, 2, 1]]

# It shouldn’t take long to evaluate which is best by measuring
# each of the lengths one by one and comparing what we find for
# each of them. This is called a brute force solution.


# Sometimes a brute force solution is exactly the right approach.
# They tend to be easy to write code for, and they work reliably.
# Their major weakness is their runtime, which is never better
# and usually much worse than algorithmic solutions.

# You should’ve noticed the pattern here: when we have N cities
# to visit, the total number of possible itineraries is N × (N–1) ×
# (N–2) × . . . × 3 × 2 × 1, otherwise known as N! (“N factorial”).

# If we look at factorials of numbers, they grow rapidly.
# This phenomenon is called combinatorial explosion.
# Combinatorial explosion doesn’t have a rigorous mathematical
# definition, but it refers to cases like this, in which apparently
# small sets can, when considered in combinations and
# permutations, lead to a number of possible choices far beyond
# the size of the original set and beyond any size that we know
# how to work with using brute force.