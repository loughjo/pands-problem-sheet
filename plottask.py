# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author : John Loughnane

from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4, 0.1)
y1 = x
y2 = x**2
y3 = x**3
#print('Values of x: ', x)
#print('Values of y: ', y1,y2,y3)
plt.plot(x, y1, color='b')
plt.plot(x, y2, color="r")
plt.plot(x, y3, color = "c")
plt.title("Plot of the functions f(x)=x, g(x)=x2 and h(x)=x3", fontsize = 14, fontweight ="bold")
plt.xlabel("Values of x", fontsize = 12)
plt.ylabel("Values of y", fontsize = 12)
plt.legend(["f(x)=x", "g(x)=x2", "h(x)=x3"], fontsize = 10)
plt.show()