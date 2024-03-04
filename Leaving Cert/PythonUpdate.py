from pandas import *
import statistics


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

def audio(a1):
    if a1 == 'Y' or a1 == 'y':
        R2 = int(input("What did you did you listen to\n1 = Music\n2 = Podcast\n3 = eBook\n"))
    if R2 == 1:
        print("Music")
    if R2 == 2:
        print("Podcast")
    if R2 == 3:
        print("eBook")
a1 = str(input("Did you listen to any audio while on the walk such as music/podcast/e-book?\nPlease enter Y/N: "))
audio(a1)

# What if / See if user reached the daily goal of amount of steps needed daily
daily = 7500
def steps(s1):
    if s1 >= daily:
        print("Well done! You reach the desired amount of steps for today")
    elif s1 < daily:
        s2 = str(input("Don't worry! Some days we don't get the results we want.\nWant soultions on how to improve? Y/N"))
    if s2
s1 = int(input('How many steps did you take today'))