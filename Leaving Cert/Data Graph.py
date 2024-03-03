import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv('data_steps-2.csv')

# Step 2: Extract Data
x1_values = df['steps']
x2_values = df['light']
y_values = df['time (seconds)']

# Step 3: Plot the Data
plt.figure(figsize=(16, 12))  # Adjust size if needed
plt.plot(x1_values, y_values, label='Steps', color='blue')
plt.plot(x2_values, y_values, label='Light Level', color='red')

# Customize your plot (labels, title, legend, etc.)
plt.xlabel('Steps and Light Level')
plt.ylabel('Time (seconds)')
plt.title('Step Tracker')
plt.legend()

# Set x-axis ticks to go in intervals of 50
plt.xticks(range(0, max(max(x1_values), max(x2_values)) + 1, 50))

# Include specific values on the x-axis without overlapping
specific_values = [654, 120]
plt.xticks(list(plt.xticks()[0])[:-1] + specific_values + [max(max(x1_values), max(x2_values))])

# Set x-axis limit to include the specific values
plt.xlim(0, max(max(x1_values), max(x2_values)))

# Show plot
plt.show()
