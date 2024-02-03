import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
sizes = [30, 60, 90, 120, 150]  # Size of bubbles
colors = ["red", "green", "blue", "orange", "purple"]  # Color of bubbles

# Create a figure and a set of subplots (one subplot in this case)
fig, ax = plt.subplots()

# Create the bubble chart
scatter = ax.scatter(x, y, s=sizes, c=colors, alpha=0.5, label="Data Points")

# Customize the chart
ax.set_title("Bubble Chart")
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")

# Create a legend
legend = ax.legend(*scatter.legend_elements(), title="Categories")
ax.add_artist(legend)

# Show the chart
plt.show()
