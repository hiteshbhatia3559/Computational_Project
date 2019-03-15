import random
import math

N = int(round(input("How many events per sample calculation?")))
counter_set = set()
for j in range(0,101):
    counter = 0
    for i in range(0, N):
        if math.hypot(random.uniform(-1, 1), random.uniform(-1, 1)) <= 1:
            counter += 1
    counter_set.add(counter)
print(counter_set)
