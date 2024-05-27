# a function that relates the taxation rate to
# the revenue collected

import math
import matplotlib.pyplot as plt


def revenue(tax):
    return(100 * (math.log(tax+1) - (tax - 0.2)**2 + 0.04))


# When country has 70 percent tax on income
# xs = [x/1000 for x in range(1001)]
# ys = [revenue(x) for x in xs]
# plt.plot(xs,ys)
# plt.plot(current_rate,revenue(current_rate),'ro')
# plt.title('Tax Rates and Revenue')
# plt.xlabel('Tax Rate')
# plt.ylabel('Revenue')
# plt.show()


# A derivative is a
# measurement of the slope of a tangent line, with large values
# denoting steepness and negative values denoting downward
# motion.


# We used four rules of calculus to derive that function. First, we
# used the rule that the derivative of log(x) is 1/x. That’s why the
# derivative of log(tax + 1) is 1/(tax + 1). Another rule is that the
# derivative of x is 2x. That’s why the derivative of (tax – 0.2) is
# 2(tax – 0.2). Two more rules are that the derivative of a
# constant number is always 0, and the derivative of 100f(x) is
# 100 times the derivative of f(x). If you combine all these rules,
# you’ll find that our tax-revenue function, 100(log(tax + 1) –
# (tax – 0.2) + 0.04), has a derivative equal to the following, as
# described in the Python function:
def revenue_derivative(tax):
    return(100 * (1/(tax + 1) - 2 * (tax - 0.2)))


# a small step from
# where are in the direction of decreased taxation, revenue
# should increase.
print(revenue_derivative(0.7))
print(revenue_derivative(0.3))
print(revenue_derivative(0.1))


# For better maximazition, we can adjust step size:
step_size = 0.001

# now we can generate next maximum
current_rate = 0.7
for i in range(20):
    current_rate = current_rate + step_size * revenue_derivative(current_rate)
    print(current_rate, revenue(current_rate))


# After our functions, we can generate an algorihm to find maximum revenue

# In practice,
# it’s quite likely that we’ll be asymptotically approaching the
# maximum: getting closer and closer to it but always remaining
# microscopically distant. So although we may never reach the
# maximum, we can get close enough that we match it up to 3 or
# 4 or 20 decimal places

# For that, we can just adjust threshold:
threshold = 0.0001

# Algorithm:
maximum_iterations = 100000
keep_going = True
iterations = 0
while(keep_going):
    rate_change = step_size * revenue_derivative(current_rate)
    current_rate = current_rate + rate_change

    if(abs(rate_change) < threshold):
        keep_going = False
    if(iterations >= maximum_iterations):
        keep_going = False

    iterations = iterations+1

print(current_rate, revenue(current_rate))

# Though humble in appearance and simple in concept, gradient
# ascent is an algorithm, just like the algorithms described in
# previous chapters. Unlike most of those algorithms, though,
# gradient ascent is in common use today and is a key part of
# many of the advanced machine learning methods that
# professionals use daily.
