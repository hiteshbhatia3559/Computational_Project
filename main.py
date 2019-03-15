import random
import math
import statistics
import matplotlib.pyplot as plt

N = int(input("How many events per sample calculation?\n"))
counter_set = []
for j in range(0,101):
    counter = 0
    for i in range(0, N):
        if math.hypot(random.uniform(-1, 1), random.uniform(-1, 1)) <= 1:
            counter += 1
    counter_set.append(counter)

mean = statistics.mean(counter_set)
mean_line = []
for i in range(0,len(counter_set)):
    mean_line.append(mean)

plt.plot(counter_set,'bo')
plt.plot(mean_line,'r+')
plt.savefig('saved.png')