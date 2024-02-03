import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Sample data for three data sets
x1 = np.random.rand(50)  # X coordinates for data set 1
y1 = np.random.rand(50)  # Y coordinates for data set 1
z1 = np.random.rand(50)  # Z coordinates for data set 1

x2 = np.random.rand(50) + 1  # X coordinates for data set 2 (shifted for visibility)
y2 = np.random.rand(50) + 1  # Y coordinates for data set 2 (shifted for visibility)
z2 = np.random.rand(50)  # Z coordinates for data set 2

x3 = np.random.rand(50)  # X coordinates for data set 3
y3 = np.random.rand(50) + 1  # Y coordinates for data set 3 (shifted for visibility)
z3 = np.random.rand(50) + 1  # Z coordinates for data set 3 (shifted for visibility)

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Create the scatter plots for each data set
ax.scatter(x1, y1, z1, c="r", marker="o", label="Data Set 1")
ax.scatter(x2, y2, z2, c="g", marker="s", label="Data Set 2")
ax.scatter(x3, y3, z3, c="b", marker="^", label="Data Set 3")

# Customize the chart
ax.set_title("3D Scatter Chart with Multiple Data Sets")
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")
ax.set_zlabel("Z-axis Label")
ax.legend()

# Show the chart
plt.show()
