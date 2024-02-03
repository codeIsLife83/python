import matplotlib.pyplot as plt

# Sample data
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]  # These values should sum up to 100%

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create the pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add a title
ax.set_title('Pie Chart Example')

# Show the chart
plt.show()
