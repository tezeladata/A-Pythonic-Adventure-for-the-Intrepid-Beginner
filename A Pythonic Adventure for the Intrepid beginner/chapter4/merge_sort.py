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


# newcabinet = [] This will be result in the end

# Our staring arrays (sorted)
# left = [1,3,4,4,5,7,8,9]
# right = [2,4,6,7,8,8,10,12,13,14] 


# Main logic:
# if left[0] > right[0]:
#     to_insert = right.pop(0)
#     newcabinet.append(to_insert)

# elif left[0] <= right[0]:
#     to_insert = left.pop(0)
#     newcabinet.append(to_insert)


# This process—checking the first elements of the left and right
# cabinets and popping the appropriate one into the new cabinet
# —needs to continue as long as both of the cabinets still have at
# least one file. 
# while(min(len(left),len(right)) > 0):
#     if left[0] > right[0]:
#         to_insert = right.pop(0)
#         newcabinet.append(to_insert)

#     elif left[0] <= right[0]:
#         to_insert = left.pop(0)
#         newcabinet.append(to_insert)

# When one array is empty and second one is not:
# if(len(left) > 0):
#     for i in left:
#         newcabinet.append(i)

# if(len(right) > 0):
#     for i in right:
#         newcabinet.append(i)


# def merging(left,right):
#     newcabinet = []

#     while(min(len(left),len(right)) > 0):
#         if left[0] > right[0]:
#             to_insert = right.pop(0)
#             newcabinet.append(to_insert)

#         elif left[0] <= right[0]:
#             to_insert = left.pop(0)
#             newcabinet.append(to_insert)


#     if(len(left) > 0):
#         for i in left:
#             newcabinet.append(i)
#     if(len(right)>0):
#         for i in right:
#             newcabinet.append(i)

#     return(newcabinet)


# left = [1,3,4,4,5,7,8,9]
# right = [2,4,6,7,8,8,10,12,13,14]
# newcab=merging(left,right)
# print(newcab)



# New function:
# If we pass a two-element list to our merge sort function, we can split
# that list into two one-element lists (that are therefore already
# sorted) and call our merging function on those one-element
# lists to get a final, sorted two-element list.

# import math
# def mergesort_two_elements(cabinet):
#     newcabinet = []

#     if(len(cabinet) == 1):
#         newcabinet = cabinet
#     else:
#         left = cabinet[:math.floor(len(cabinet)/2)]
#         right = cabinet[math.floor(len(cabinet)/2):]
#         newcabinet = merging(left,right)
#     return(newcabinet)

# Now we can write function for four element array, but breakthrough comes, when we realise, that we can use recursion. 



# Final result:

# Inner fund:
def merging(left,right):
    newcabinet = []

    while(min(len(left),len(right)) > 0):
        if left[0] > right[0]:
            to_insert = right.pop(0)
            newcabinet.append(to_insert)
        elif left[0] <= right[0]:
            to_insert = left.pop(0)
            newcabinet.append(to_insert)


    if(len(left) > 0):
        for i in left:
            newcabinet.append(i)
    if(len(right) > 0):
        for i in right:
            newcabinet.append(i)

    return(newcabinet)

# main func:
import math
def mergesort(cabinet):
    newcabinet = []

    if(len(cabinet) == 1):
        newcabinet=cabinet
    else:
        left = mergesort(cabinet[:math.floor(len(cabinet)/2)])
        right = mergesort(cabinet[math.floor(len(cabinet)/2):])
        newcabinet = merging(left,right)

    return(newcabinet)


cabinet = [4,1,3,2,6,3,18,2,9,7,3,1,2.5,-9]
newcabinet=mergesort(cabinet)
print(newcabinet)


# The number of times a list
# of length n can be split in half before each sublist has only one
# element is about log(n) (where the log is to base 2), and the
# number of comparisons we have to make at each merge is at
# most n. So n or fewer comparisons for each of log(n)
# comparisons means that merge sort is O(n×log(n))