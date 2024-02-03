import matplotlib.pyplot as plt

# Sample data
categories = ["Category A", "Category B", "Category C", "Category D"]
values = [15, 30, 45, 10]

# Create a figure and a set of subplots (one subplot in this case)
fig, ax = plt.subplots()

# Create the bar chart
ax.bar(categories, values, color="blue", alpha=0.7)

# Customize the chart
ax.set_title("Bar Chart")
ax.set_xlabel("Categories")
ax.set_ylabel("Values")

# Show the chart
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
