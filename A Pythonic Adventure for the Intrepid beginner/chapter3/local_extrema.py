import math

# We may perform gradient ascent
# perfectly, but realize that the peak we have reached at the end
# is only a “local” peak—it’s higher than every point around it,
# but not higher than some faraway global maximum.

def income(edu_yrs):
    return(math.sin((edu_yrs - 10.6) * (2 * math.pi/4)) + (edu_yrs - 11)/2)


import matplotlib.pyplot as plt
xs = [11 + x/100 for x in list(range(901))]
ys = [income(x) for x in xs]
plt.plot(xs,ys)
current_edu = 12.5
plt.plot(current_edu,income(current_edu),'ro')
plt.title('Education and Income')
plt.xlabel('Years of Education')
plt.ylabel('Lifetime Income')
plt.show()


# Graduation from high school—12 years—is an important
# milestone and should correspond to higher earnings than
# dropping out. In other words, it’s a maximum, but importantly
# it’s only a local maximum. Getting more than 12 years of
# education is helpful, but not at first.


def income_derivative(edu_yrs):
    return(math.cos((edu_yrs - 10.6) * (2 * math.pi/4)) + 1/2)

threshold = 0.0001
maximum_iterations = 100000
current_education = 12.5
step_size = 0.001
keep_going = True
iterations = 0


while(keep_going):
    education_change = step_size * income_derivative(current_education)
    current_education = current_education + education_change


    if(abs(education_change) < threshold):
        keep_going = False

    if(iterations >= maximum_iterations):
        keep_going=False

    iterations = iterations + 1

# The code in here follows exactly the same gradient ascent
# algorithm as the revenue-maximization process we
# implemented previously.

# If we are
# naive and trust the gradient ascent algorithm too much, we
# might recommend that college freshmen drop out and join the
# workforce immediately to maximize earnings at this local
# maximum.

# a. An advanced version of gradient ascent, called
# stochastic gradient ascent, incorporates randomness for this
# reason, and other algorithms, like simulated annealing, do the
# same.



# One way to do it is to “flip” our function or, more
# precisely, to take its negative.