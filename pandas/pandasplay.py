import pandas as pd


data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"],
}
df = pd.DataFrame(data)

# Display the dataframe
print(df)

# Add a new column
df["Salary"] = [50000, 60000, 70000, 80000]

# Display the dataframe with the new column
print(df)

# Filter rows based on condition
filtered_df = df[df["Age"] > 30]
print(filtered_df)

# Calculate basic statistics
print(df.describe())

# Save the dataframe to a CSV file
df.to_csv("output.csv", index=False)
