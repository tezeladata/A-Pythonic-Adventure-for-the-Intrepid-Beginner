# Could we find some
# holy grail algorithm that could sort any possible list in fewer
# than 10 steps?


# Merge sort is an algorithm that’s much quicker than insertion
# sort. Just like insertion sort, merge sort contains two parts: a
# part that merges two lists and a part that repeatedly uses
# merging to accomplish the actual sorting.

# If we have two sorted arrays and we want to combine them, we use merge sort

# Without first writing code, we can imagine our scenario:
# we have two sorted arrays and we take third one, which is empty at the beginning.
# We can call our sorted arrays names, "left" and "right"



# To merge, we can take the first file in both of the original
# cabinets simultaneously: the first left file with our left hand and
# the first right file with our right hand. Whichever file is lower is
# inserted into the new cabinet as its first file. To find the second
# file for the new cabinet, once again take the first file in the left
# and right cabinets, compare them, and insert whichever is
# lower into the last position in the new cabinet. When either the
# left cabinet or the right cabinet is empty, take the remaining
# files in the non-empty cabinet and place them all together at
# the end of the new cabinet.


newcabinet = [] #This will be result in the end

# Our staring arrays (sorted)
left = [1,3,4,4,5,7,8,9]
right = [2,4,6,7,8,8,10,12,13,14] 

