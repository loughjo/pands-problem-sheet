# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author : John Loughnane

#
# import matplotlib.pylot library so we can make the plots
import numpy as np
import matplotlib.pyplot as plt

# np.arrange() method creates an array which Starts at 0 and Stops at 4.1 in steps of 0.1.
# The highest value 4.1 isn't included and these values are assigned to the variable x
xpoints = np.arange(0, 4.1, 0.1)

# Here we get f(x) and assign these points to ypoints1.
# We now get g(x) = x2 by getting each xpoints value and multiplying by the power of 2 and assigning the values to ypoints2 to plot
# Next h(x)=x3 get each xpoints value and multiply by the power of 3 and assign the values to ypoints3 to plot
ypoints1 = xpoints
ypoints2 = xpoints**2
ypoints3 = xpoints**3

# The plot() function is used to draw the points and use the argument color to change the color for each plot - blue (b), red (r) and cyam (c). 
# 
plt.plot(xpoints, ypoints1, color ='b')
plt.plot(xpoints, ypoints2, color ='r')
plt.plot(xpoints, ypoints3, color ='c')

# This part of the code makes use of matplotlib.pyplot to add a Title, X and Y Labels and a legend to the graph.
# We can also change the fontsize on the plot
plt.title("Plot of the functions f(x)=x, g(x)=x2 and h(x)=x3", fontsize = 14, fontweight ="bold")
plt.xlabel("Values of x", fontsize = 12)
plt.ylabel("Values of y", fontsize = 12)
plt.legend(["f(x)=x", "g(x)=x2", "h(x)=x3"], fontsize = 10)

# The show function is used to display the plot.
plt.show()