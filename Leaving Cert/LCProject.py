import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
dataIn = pd.read_csv('Micro-BIT Data.csv')

# Step 2: Extract Data
xSteps = dataIn['steps']
xLight = dataIn['light']
xTemp = dataIn['temp']  
yTime = dataIn['time (seconds)'] / 60

# Plot the Data
plt.figure(figsize=(16, 10))  
plt.plot(xSteps, yTime, label='Steps', color='blue')
plt.plot(xLight, yTime, label='Light Level', color='yellow')
plt.plot(xTemp, yTime, label='Temp Level', color='red')

# Customize the plot (labels, title and legend))
plt.xlabel('Steps, Light Level, and Temp Level')
plt.ylabel('Time (minutes)')
plt.title('Step Tracker')
plt.legend()

# Set x-axis ticks to go in intervals of 500
plt.xticks(range(0, max(max(xSteps), max(xLight), max(xTemp)) + 1, 500))

# Include specific values on the x-axis without overlapping
specific_values = [8523, 158, 9]
plt.xticks(list(plt.xticks()[0])[:-1] + specific_values + [max(max(xSteps), max(xLight), max(xTemp))])

# Set x-axis limit to include the specific values
plt.xlim(0, max(max(xSteps), max(xLight), max(xTemp)))

# Show plot
#plt.show()


# Print last digit of the data
print("\033[94mSteps\033[0m") # Blue colour text
print("Average value of steps column:", dataIn['steps'].mean())
print("Median value of steps column:", dataIn['steps'].median())
print("Mode value of steps column:", dataIn['steps'].mode())
print("Max value of steps column:", dataIn['steps'].max())

print("\033[95mTime in seconds\033[0m") # Red colour text
print("Average value of time (seconds) column:", dataIn['time (seconds)'].mean())
print("Median value of time (seconds) column:", dataIn['time (seconds)'].median())
print("Mode value of time (seconds) column:", dataIn['time (seconds)'].mode())
print("Max value of time (seconds) column:", dataIn['time (seconds)'].max())

print("\033[91mLight Level\033[0m") # Pink colour text
print("Average value of light column:", dataIn['light'].mean())
print("Median value of light column:", dataIn['light'].median())
print("Mode value of light column:", dataIn['light'].mode())
print("Max value of light column:", dataIn['light'].max())


print("\033[33mTemperature Level\033[0m") # Orange colour text
print("Average value of temp column:", dataIn['temp'].mean())
print("Median value of temp column:", dataIn['temp'].median())
print("Mode value of temp column:", dataIn['temp'].mode())
print("Max value of temp column:", dataIn['temp'].max())

# What if user doesn't reach average steps
# - TheyTime are unactive,moderate,active
# Data online
steps = 7500
steps2 = 10000
time = 69
# Data from file
xSteps = dataIn['steps'].max()
xLight = dataIn['light'].max() 
xTemp = dataIn['temp'].max() 
yTime = dataIn['time (seconds)'].max()/60  


yTime = round(yTime)
newTime = time - yTime
newTime2 = (time - yTime)*(-1)
belSteps = steps - xSteps
aboSteps = (steps - xSteps)*(-1)

def active(userName,xSteps,yTime):
    print("Hello",userName)
    if yTime < time:
        print(f"{userName} try to walk for", newTime, "minutes more!")
    elif yTime == time:
        print(f"{userName}, well done you reached the daily goal!")
    elif yTime > time:
        print(f"{userName}, excellent! You walked past your daily goal by", newTime2, "minutes!")
        
    if xSteps < steps:
        print(f"{userName} try to walk {belSteps} steps more!")
    elif xSteps == steps:
        print(f"{userName} well done you reached the daily goal of {steps} steps!")
    elif xSteps > steps:
        print(f"{userName}, excellent! You walked past your daily goal by {aboSteps} steps!")
    elif xSteps > steps:
        print(f"{userName}, amazing! You walked exceeded your daily goal by {aboSteps} steps!")
userName = str(input('Enter your name: '))
active(userName,xSteps,yTime)

# Expand
# How active do yTimeou want to be per week e.g. float(5.5 hours)
