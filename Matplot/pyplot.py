# Import necessary libraries
import matplotlib.pyplot as pl
import numpy as np

# Define points
xp = np.array([0,10])
yp = np.array([0,100])

# Plot the points
pl.plot(xp,yp)

# Save the plot to a file
pl.savefig('pyplot.png')

# Optionally display the plot
pl.show()
