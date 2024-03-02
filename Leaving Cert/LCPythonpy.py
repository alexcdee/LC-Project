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

def audio(a1):
    if a1 == 'Y' or a1 == 'y':
        R2 = int(input("What did you did you listen to\n1 = Music\n2 = Podcast\n3 = eBook\n"))
    if R2 == 1:
        print("Music")
    if R2 == 2:
        print("Podcast")
    if R2 == 3:
        print("eBook")
    
    '''
    if R1 == 5:
        print("That's great!")
    elif R1 == 4:
        print("")
    elif R1 == 3:
        print("")
    elif R1 == 2:
        print("")
    elif R1 == 1:
        print("")
      '''  
    
    



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
a1 = str(input("Did you listen to any audio while on the walk such as music/podcast/e-book?\nPlease enter Y/N: "))
audio(a1)