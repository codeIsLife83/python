import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and a set of subplots (one subplot in this case)
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Customize the chart
ax.set_title("Simple Line Chart")
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")

# Show the chart
plt.show()
