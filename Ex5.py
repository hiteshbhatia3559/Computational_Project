import random
import statistics
import matplotlib.pyplot as plt
import math


def move(last):
    if random.randint(0, 1) == 0:
        last -= 1
    else:
        last += 1
    return last

def calculate_plot(list_of_i):
    dict_of_values = []
    for N in list_of_i:
        pass
    pass

# Uncomment this for Ex5.a
# last = 0
# positions = []
# for i in range(0,1001):
#     last = move(last)
#     positions.append(last)
#
# plt.plot(positions)
# plt.savefig('Ex5a.png')
