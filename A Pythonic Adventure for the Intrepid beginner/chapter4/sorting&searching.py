import random

# Several methods for sorting and searching are among these
# fundamental algorithms.

# we’ll also use this
# chapter to discuss algorithm speed and the special notation we
# use to compare algorithms’ efficiencies.

# Whatever method you follow as you sort the filing cabinet, we
# can describe it as a “sorting algorithm.”



# How insertion sort works:
# 1. Select the highest file in the filing cabinet. (We’ll start at
# the back of the cabinet and work our way to the front.)
# 2. Compare the file you have selected with the file to
# insert.
# 3. If the file you have selected is lower than the file to
# insert, place the file to insert one position behind that
# file.
# 4. If the file you have selected is higher than the file to
# insert, select the next highest file in the filing cabinet.
# 5. Repeat steps 2 to 4 until you have inserted your file or
# compared it with every existing file. If you have not yet
# inserted your file after comparing it with every existing
# file, insert it at the beginning of the filing cabinet.


# The logic for insertion sort:
cabinet = [1,2,3,3,4,6,8,12]
to_insert = 5

# We proceed one at a time through every number in the list
# (every file in the cabinet).

# Starting from the end of a list
check_location = len(cabinet) - 1

# We’ll also define a variable called insert_location. The goal of
# our algorithm is to determine the proper value of
# insert_location, and then it’s a simple matter of inserting the
# file at the insert_location. 
insert_location = 0


if to_insert > cabinet[check_location]:
    insert_location = check_location + 1

cabinet.insert(insert_location,to_insert)
print(cabinet)

# As we can see, only one iteration does not work, so we need functions with loop.
# This function combines all of the previous
# code and also adds a while loop

def insert_cabinet(cabinet,to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0


    while(check_location >= 0):
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = - 1
        check_location = check_location - 1

    cabinet.insert(insert_location,to_insert)
    return(cabinet)


cabinet = [1,2,3,3,4,6,8,12]
newcabinet = insert_cabinet(cabinet,1)
print(newcabinet)




# Now about insertion sort. We take one item from unsorted list, find it's position and insert it. This taking
# and inserting goes on, until the list is sorted

# First of all, we start with unsorted list and empty list
cabinet = [8,4,6,1,2,5,3,7]
newcabinet = []

# After we use pop(),
# cabinet no longer contains that element, and we store it in the
# variable to_insert so that we can put it into the newcabinet.
to_insert = cabinet.pop(0)
newcabinet = insert_cabinet(newcabinet, to_insert)

print(newcabinet)



# We can now create insertion sort function
cabinet = [8,4,6,1,2,5,3,7]
def insertion_sort(cabinet):
    newcabinet = []

    while len(cabinet) > 0:
        to_insert = cabinet.pop(0)
        newcabinet = insert_cabinet(newcabinet, to_insert)

    return(newcabinet)

sortedcabinet = insertion_sort(cabinet)
print(sortedcabinet)

print(insertion_sort([random.randint(0, 10000) for _ in range(100)]))


# Insertion sort works—it sorts lists—so it’s good in the sense
# that it accomplishes its purpose. Another point in its favor is
# that it’s easy to understand and explain with reference to
# physical tasks that many people are familiar with.

# However, insertion sort has one crucial failing: it takes a long
# time to perform.



# The final reason to create faster algorithms is the same reason
# that people try to do better in any pursuit. Even though there is
# no obvious need for it, people try to run the 100-meter dash
# faster, play chess better, and cook a tastier pizza than anyone
# ever has before.





# MEASURING TIME PRECISELY

from timeit import default_timer as timer
start = timer()
cabinet = [8,4,6,1,2,5,3,7]
sortedcabinet = insertion_sort(cabinet)
end = timer()
print(end - start)



# we added stepcounter variable, to see how many steps are made during function's work
def insert_cabinet(cabinet,to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    global stepcounter

    while(check_location >= 0):
        stepcounter += 1
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = - 1
        check_location = check_location - 1
    
    stepcounter += 1
    cabinet.insert(insert_location,to_insert)
    return(cabinet)

def insertion_sort(cabinet):
    newcabinet = []
    global stepcounter

    while len(cabinet) > 0:
        stepcounter += 1
        to_insert = cabinet.pop(0)
        newcabinet = insert_cabinet(newcabinet,to_insert)
    return(newcabinet)


cabinet = [8,4,6,1,2,3,7]
stepcounter = 0
sortedcabinet = insertion_sort(cabinet)
print(stepcounter)



# Instead of manually writing out each unsorted list, we
# can use a simple list comprehension in Python to generate a
# random list of any specified length.

import random
size_of_cabinet = 10
cabinet = [int(1000 * random.random()) for i in
range(size_of_cabinet)]

def check_steps(size_of_cabinet):
    cabinet = [int(1000 * random.random()) for i in range(size_of_cabinet)]
    global stepcounter

    stepcounter = 0
    sortedcabinet = insertion_sort(cabinet)
    return(stepcounter)

random.seed(5040)
xs = list(range(1,100))
ys = [check_steps(x) for x in xs]
print(ys)


# For visualization:
import matplotlib.pyplot as plt
import math
# plt.plot(xs,ys)
# plt.title('Steps Required for Insertion Sort for Random Cabinets')
# plt.xlabel('Number of Files in Random Cabinet')
# plt.ylabel('Steps Required to Sort Cabinet by Insertion Sort')
# plt.show()


# Saying that the plot gets gradually steeper as the list length
# increases is still not as precise as we want to be. 


# Does the number of steps required for insertion
# sort follow this exponential function that we could say fits the
# narrowest possible definition of exponential growth? We can
# get a clue about the answer by plotting our step curve together
# with an exponential growth curve, as follows

import numpy as np
random.seed(5040)
xs = list(range(1,100))
ys = [check_steps(x) for x in xs]
ys_exp = [math.exp(x) for x in xs]
plt.plot(xs,ys)
axes = plt.gca()
axes.set_ylim([np.min(ys),np.max(ys) + 140])
plt.plot(xs,ys_exp)
plt.title('Comparing Insertion Sort to the Exponential Function')
plt.xlabel('Number of Files in Random Cabinet')
plt.ylabel('Steps Required to Sort Cabinet')
plt.show()


random.seed(5040)
xs = list(range(1,100))
ys = [check_steps(x) for x in xs]
xs_exp = [math.exp(x) for x in xs]
xs_squared = [x**2 for x in xs]
xs_threehalves = [x**1.5 for x in xs]
xs_cubed = [x**3 for x in xs]
plt.plot(xs,ys)
axes = plt.gca()
axes.set_ylim([np.min(ys),np.max(ys) + 140])
plt.plot(xs,xs_exp)
plt.plot(xs,xs)
plt.plot(xs,xs_squared)
plt.plot(xs,xs_cubed)
plt.plot(xs,xs_threehalves)
plt.title('Comparing Insertion Sort to Other Growth Rates')
plt.xlabel('Number of Files in Random Cabinet')
plt.ylabel('Steps Required to Sort Cabinet')
plt.show()



# If we want to see all of the steps, we can look at the following:

# Steps required for pulling files: n (1 step for pulling eachof n files)
# Steps required for comparison: up to 1 + 2 + . . . + (n –1)
# Steps required for inserting files: n (1 step for insertingeach of n files)

# maximum_total_steps = ((n**2) / 2) + (3n / 2)