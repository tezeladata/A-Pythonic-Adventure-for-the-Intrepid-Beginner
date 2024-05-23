import matplotlib.pyplot as plt # For visual representation

# An algorithm is a finite set of rules that gives a sequence of operations for solving a specific type of problem.
# Taxes and some dishes, what do they have in common? People prepare both by following instructions

# In addition to defining algorithm, the great computer scientist
# Donald Knuth noted that it is nearly synonymous with recipe,
# procedure, and rigmarole. 
# As we learn more about algorithms, we will see them everywhere


# the parabolic arch employs the principle that when weight is uniformly applied above, the internal compression (see line of thrust) resulting from that weight will follow a parabolic curve.





# The analytic approach of the outfielder problem

# Going back to Galileo's Italy, there was formula for ball's horizontal position at exact time:
# x = v1 * t
# x is horizontal position
# v1 is starting speed at horizontal direction
# t is time

# Additionally, there was also formula for height:
# y = (v2 * t) + ((a * t**2) / 2)
# y is height position
# v2 is starting speed in vertical direction
# a is acceleration

# If we substitute first formula into second one, we can see that height is relative to horizontal position:
# y = ((v2 / v1) * x) + ((a * x**2) / (2 * v1 ** 2))

# After inserting speed values in formula (v1 = 0.99, v2 = 9.99), we get following result for location variable
def ball_trajectory(x):
    location = 10*x - 5*(x**2)
    return location

# For visualization
xs = [x/100 for x in list(range(201))] # 200 x values
ys = [ball_trajectory(x) for x in xs] # 200 y values, which will depend on corresponding x. In this case, ball_trajectory(x)
plt.plot(xs, ys)


# The solve-for-x strategy is
# extremely common in the hard sciences, at both the high school
# and college levels.

# We write down equation and solve it for variable we are interested in
# In this case:
# 10x - 5x^2 = 0  -- x=0 and x=2

# The solve-for-x strategy is easy in this case because we already
# know the equation that needs to be solved and the method to
# solve it. 

# Solving the mystery of where a
# ball will land doesn’t provide a clear-cut answer to the
# outfielder problem—that is, how a human can instinctively
# know where a ball will land without plugging it into a computer
# program.

# The manifest ability of dogs to catch Frisbees and humans to
# catch baseballs seems to be a point in favor of the inner
# physicist theory. 





# The Algorithmic Approach
# Adding lines of horizontal movement
xs2 = [0.1,2]
ys2 = [ball_trajectory(0.1),0]
xs3 = [0.2,2]
ys3 = [ball_trajectory(0.2),0]
xs4 = [0.3,2]
ys4 = [ball_trajectory(0.3),0]
plt.plot(xs,ys,xs2,ys2,xs3,ys3,xs4,ys4)

# Straight lines represent moment, when outfielder looks at ball
xs5 = [0.3,0.3]
ys5 = [0,ball_trajectory(0.3)]
xs6 = [0.3,2]
ys6 = [0,0]
plt.title('The Trajectory of a Thrown Ball - Tangent Calculation')
plt.xlabel('Horizontal Position of Ball')
plt.ylabel('Vertical Position of Ball')
plt.plot(xs,ys,xs4,ys4,xs5,ys5,xs6,ys6)
plt.text(0.31,ball_trajectory(0.3)/2,'A',fontsize = 16)
plt.text((0.3 + 2)/2,0.05,'B',fontsize = 16)
plt.show()


# We can calculate ball's angle at each moment using following formula:
# res = (10*x - 5*x*x) / (2 - x) = 5x

# After conclusions, we can see, that angle of ball grows at constant rate, so it has 0 acceleration.
# If we stay at correct place, we can see, that ball's angle experiences zero acceleration
# If we stay too close, we will see acceleration. But if we stay far away, we'll see deceleration

# Five step process  doesn’t rely on a solve-for-x strategy or any
# explicit equation at all. Instead, it proposes successive
# iterations of easy observations and small, gradual steps to
# reach a well-defined goal. In other words, the process that we
# have inferred from Chapman’s theory is an algorithm.





# The word algorithm came from the name of the great al Khwarizmi.
# Algorithms exist at the edge of
# what is possible, and every time an algorithm is created or
# improved, we push the frontier of efficiency and knowledge out
# a little further.

# an algorithm should not only be used as a tool, but also as a
# formidable problem that was solved