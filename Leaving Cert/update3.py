import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv('data_with_one_hour.csv')

# Step 2: Extract Data
x1 = df['steps']
x2 = df['light']
x3 = df['temp']  # Assuming 'temp' is the column name in your CSV file
y = df['time (seconds)'] / 60

# Step 3: Plot the Data
plt.figure(figsize=(10, 6))  # Adjust size if needed
plt.plot(x1, y, label='Steps', color='blue')
plt.plot(x2, y, label='Light Level', color='red')
plt.plot(x3, y, label='Temp Level', color='orange')

# Customize your plot (labels, title, legend, etc.)
plt.xlabel('Steps, Light Level, and Temp Level')
plt.ylabel('Time (minutes)')
plt.title('Step Tracker')
plt.legend()

# Set x-axis ticks to go in intervals of 50
plt.xticks(range(0, max(max(x1), max(x2), max(x3)) + 1, 50))

# Include specific values on the x-axis without overlapping
specific_values = [654, 120, 23]  # Add 23 to the specific values
plt.xticks(list(plt.xticks()[0])[:-1] + specific_values + [max(max(x1), max(x2), max(x3))])

# Set x-axis limit to include the specific values
plt.xlim(0, max(max(x1), max(x2), max(x3)))

# Show plot
#plt.show()

# Print last digit of the data
print("\033[94mSteps\033[0m") # Blue colour text
last_steps_value = df['steps'].iloc[-1]
print("Last value of steps column:", last_steps_value)
print("Average value of steps column:", df['steps'].mean())
print("Median value of steps column:", df['steps'].median())
print("Max value of steps column:", df['steps'].max())

print("\033[95mTime in seconds\033[0m") # Red colour text
last_seconds_value = df['time (seconds)'].iloc[-1]
print("Last value of time (seconds) column:", last_seconds_value)
print("Average value of time (seconds) column:", df['time (seconds)'].mean())
print("Median value of time (seconds) column:", df['time (seconds)'].median())
print("Max value of time (seconds) column:", df['time (seconds)'].max())

print("\033[91mLight Level\033[0m") # Pink colour text
last_light_value = df['light'].iloc[-1]
print("Last value of light column:", last_light_value)
print("Average value of light column:", df['light'].mean())
print("Median value of light column:", df['light'].median())
print("Max value of light column:", df['light'].max())


print("\033[33mTemperature Level\033[0m") # Orange colour text
last_temp_value = df['temp'].iloc[-1]
print("Last value of temp column:", last_temp_value)
print("Average value of temp column:", df['temp'].mean())
print("Median value of temp column:", df['temp'].median())
print("Max value of temp column:", df['temp'].max())

# What if user doesn't reach average steps
# - They are unactive,moderate,active
# Data online
steps = 7500
steps2 = 10000
time = 69
# Data from file
x1 = df['steps'].max()# Step 645
x2 = df['light'].max() # Light 128
x3 = df['temp'].max() # Temp 23
y = df['time (seconds)'].max()/60  #Time 355 (5.59 minutes)
y = round(y)
# Try to get to do math say userName you're only 5 minutes away etc. to reaching the goal
newTime = time - y
newTime2 = (time - y)*(-1)
belSteps = steps - x1
aboSteps = (steps - x1)*(-1)

def active(userName,x1,y):

    print("Hello",userName)
    if y < time:
        print(f"{userName} try to walk for {newTime} minutes more!")
    elif y == time:
        print(f"{userName}, well done you reached the daily goal!")
    elif y > time:
        print(f"{userName}, excellent! You walked past your daily goal by {newTime2} minutes!")
        
    if x1 < steps:
        print(f"{userName} try to walk {belSteps} steps more!")
    elif x1 == steps:
        print(f"{userName} well done you reached the daily goal of {steps} steps!")
    elif x1 > steps:
        print(f"{userName}, excellent! You walked past your daily goal by {aboSteps} steps!")
    elif x1 > steps:
        print(f"{userName}, amazing! You walked exceeded your daily goal by {aboSteps} steps!")



userName = str(input('Enter your name: '))
active(userName,x1,y)

# Expand
# How active do you want to be per week e.g. float(5.5 hours)