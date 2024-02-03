import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and a set of subplots (one subplot in this case)
fig, ax = plt.subplots()

# Create the scatter chart
ax.scatter(x, y, marker="o", color="blue", label="Data Points")

# Customize the chart
ax.set_title("Scatter Chart")
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")

# Show the chart
plt.show()
