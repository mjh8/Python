# This code simulates 1,000 random dice rolls and calculates the mean.

import random
import statistics
import numpy as np

l = []
random.seed(123)
# random.random()

for _ in range(1000):
    random_int = random.randint(1,6)
    l.append(random_int)

print(l)

# print(np.mean(l))   #First way to get Mean - Numpy Mean

def mean(x):
    mean = sum(x) / len(x)
    return mean   #Second way to get Mean - Create a Function

print(mean(l)) #Print the Mean of the Random 1,000 Numbers
print(len(l))

SD = statistics.stdev(l)
SD2 = np.std(l) #Second way to Calculate Standard Deviation

print(SD) #Print the Standard Deviation of the Random 1,000 Numbers
print(SD2)

# Print Standard Deviation Tiers

print(mean(l) - SD*3)
print(mean(l) - SD*2)
print(mean(l) - SD)
print(mean(l))
print(mean(l) + SD)
print(mean(l) + SD*2)
print(mean(l) + SD*3)