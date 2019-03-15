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
        N = math.pow(2, N)
        counter_list = []
        for j in range(0, 100):
            last = 0
            for i in range(0, int(N)):
                last = move(last)
            counter_list.append(last)
        mean = 0
        std_dev = 0
        uncertainity = 0
        try:
            mean = statistics.mean(counter_list)
            std_dev = statistics.pstdev(counter_list)
            uncertainity = std_dev / math.sqrt(mean)
        except:
            continue
        sum_of_squares = 0
        for item in counter_list:
            sum_of_squares += pow(item, 2)
        mean_of_sum_of_squares = sum_of_squares / len(counter_list)
        rms = math.sqrt(mean_of_sum_of_squares)
        dict_of_values.append({str(N): [mean, uncertainity,rms]})
    return dict_of_values


# Uncomment this block for Ex5.a
# last = 0
# positions = []
# for i in range(0,1000):
#     last = move(last)
#     positions.append(last)
#
# plt.plot(positions)
# plt.savefig('Ex5a.png')
# ----------------------------------------------------------------------------------------------------------------------
# Uncomment this block for Ex5.b and Ex5.c
calculator = calculate_plot(range(8, 14))
mean_line = []
uncertainity_line = []
rms_line = []
root_n = []
for item in calculator:
    mean_line.append(list(item.values())[0][0])
    uncertainity_line.append(list(item.values())[0][1])
    rms_line.append(list(item.values())[0][2])

for item in range(8,14):
    root_n.append(math.sqrt(item))
plt.semilogx(mean_line, uncertainity_line)
plt.savefig('Ex5b.png')
plt.semilogx(rms_line,uncertainity_line)
plt.savefig('Ex5c.png')
