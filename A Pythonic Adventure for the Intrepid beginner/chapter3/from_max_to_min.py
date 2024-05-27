# In fact, moving from maximization to minimization is quite
# simple. One way to do it is to “flip” our function or, more
# precisely, to take its negative.

import math
def revenue(tax):
    return(100 * (math.log(tax+1) - (tax - 0.2)**2 + 0.04))

def revenue_flipped(tax):
    return(0 - revenue(tax))

def revenue_derivative(tax):
    return(100 * (1/(tax + 1) - 2 * (tax - 0.2)))

import matplotlib.pyplot as plt
xs = [x/1000 for x in range(1001)]
ys = [revenue_flipped(x) for x in xs]
plt.plot(xs,ys)
plt.title('The Tax/Revenue Curve - Flipped')
plt.xlabel('Current Tax Rate')
plt.ylabel('Revenue - Flipped')
plt.show()


# The actual process of
# minimization is very similar to the process of maximization: we
# can use gradient descent instead of gradient ascent.

# In order to minimize, we move in the
# opposite direction of the gradient.

threshold = 0.0001
maximum_iterations = 10000
def revenue_derivative_flipped(tax):
    return(0-revenue_derivative(tax))

current_rate = 0.7
keep_going = True
iterations = 0
step_size = 0.001

while(keep_going):
    rate_change = step_size * revenue_derivative_flipped(current_rate)
    current_rate = current_rate - rate_change

    if(abs(rate_change) < threshold):
        keep_going = False

    if(iterations >= maximum_iterations):
        keep_going = False


    iterations = iterations + 1
    print(current_rate)


# We feel that if we are ever in a situation that requires maximization
# or minimization, we should immediately apply gradient ascent
# or descent and implicitly trust whatever results we find.

# Algorithms are powerful for practical purposes, enabling us to
# achieve goals like catching baseballs and finding revenuemaximizing taxation rates. But though algorithms can achieve
# goals effectively, they’re not as suited to the more philosophical
# task of deciding which goals are worth pursuing in the first
# place.