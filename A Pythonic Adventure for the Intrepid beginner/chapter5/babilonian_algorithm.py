# Suppose that we need to find the square root of a number x. As
# with any math problem, we can try a guess-and-check strategy.

# Let’s say that our best guess for the square root of x is some
# number y. We can calculate y , and if it’s equal to x, we’re done

# z = x / y

# You can understand why the Babylonian algorithm works if you
# consider these two simple cases:

# if y < x**0.5, then y**2 < x. So x/y**2 > 1. x * (x / y**2) > x
# But notice, that x * (x / y**2) = x**2 / y**2.  x**2 / y**2 = (x/y)**2 = z**2. So z**2 > x, z > x**0.5

# if y > x**0.5, then y**2 > x. So x/y**2 < 1. x * (x / y**2) < x
# After same simplifications, z < x**0.5

# With that simplifications, we can write, that:
# If y < x**.5, then z > x**.5
# If y > x**.5, then z < x**.5


# Step 3 of the Babylonian algorithm
# asks us to average an overestimate and an underestimate of the
# truth. The average of the underestimate and the overestimate
# will be higher than the underestimate and lower than the
# overestimate, so it will be closer to the truth than whichever of
# y or z was a worse guess

# Eventually, after many rounds of
# gradual improvement of our guesses, we arrive at the true value
# of x**.5

# In conclusion, we can implement babilonian function:

def square_root(x,y,error_tolerance):
    our_error = error_tolerance * 2
    while(our_error > error_tolerance):
        z = x/y
        y = (y + z)/2
        our_error = y**2 - x
    return y

print(square_root(20, 1, .000000000000001))
print(5**.5)