import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv('data_steps-2.csv')

# Step 2: Extract Data
x1 = df['steps']
x2 = df['light']
y = df['time (seconds)']

# Step 3: Plot the Data
plt.figure(figsize=(16, 12))  # Adjust size if needed
plt.plot(x1, y, label='Steps', color='blue')
plt.plot(x2, y, label='Light Level', color='red')

# Customize your plot (labels, title, legend, etc.)
plt.xlabel('Steps and Light Level')
plt.ylabel('Time (seconds)')
plt.title('Step Tracker')
plt.legend()

# Set x-axis ticks to go in intervals of 50
plt.xticks(range(0, max(max(x1), max(x2)) + 1, 50))

# Include specific values on the x-axis without overlapping
specific_values = [654, 120]
plt.xticks(list(plt.xticks()[0])[:-1] + specific_values + [max(max(x1), max(x2))])

# Set x-axis limit to include the specific values
plt.xlim(0, max(max(x1), max(x2)))

# Show plot
plt.show()
