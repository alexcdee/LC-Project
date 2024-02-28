from pandas import *
import statistics
import matplotlib.pyplot as plt

dataIn = read_csv("data.csv")

steps = dataIn['steps'].tolist()
print('Steps',steps)
light = dataIn['light'].tolist()
print('Lights',light)
time = dataIn['time'].tolist()
print('Time',time)
print('The mean is of steps:',round(statistics.mean(steps)))
print('The mode is of steps:',statistics.mode(steps))
print('The median is fo steps:',round(statistics.median(steps)))

'''
plt.title("Step Tracker Data", loc = 'left')
plt.plot(steps,light,time)
plt.show()
'''

# What if Questions
# #What if the user listened to music/podcast/ebook while on the walk
'''
def switch(user):
    if user == 1:
        one = input('What did you do before?' )
        return 'ok'
    elif user == 2:
        return '2'
    elif user == 3:
        return '3'
    elif user == 4:
        return '4'
    elif user == 5:
        return '5'
'''
'''
user = int(input('On a scale through 1-5. How energized do you feel after the walk/jog/run? '))
print(switch(user))
'''
