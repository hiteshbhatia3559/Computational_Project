import random
import math
import statistics
import matplotlib.pyplot as plt

# Below function takes a list of values of N
def calculate_plot(list_of_i):
    dict_of_values = []
    for N in list_of_i:
        N = int(math.pow(2, N))
        counter_list = []
        for j in range(0, 101):
            counter = 0
            for i in range(0, N):
                x_val = random.uniform(-1,1)
                y_val = random.uniform(-1,1)
                if ((x_val <=1) and (x_val >= 0)) and ((y_val <=1) and (y_val >= 0)) and (y_val <= math.pow(math.sin(1/x_val),2)):
                    counter += 1
            counter_list.append(counter)

        mean = statistics.mean(counter_list)
        std_dev = statistics.pstdev(counter_list)
        uncertainity = std_dev / math.sqrt(mean)
        dict_of_values.append({str(N):(mean,uncertainity)})
    return dict_of_values


calculator = calculate_plot(range(8, 64))

mean_line = []
uncertainity_line = []
pi_line = []
for item in calculator:
    mean, uncertainity = list(item.values())[0]
    mean_line.append(mean)
    uncertainity_line.append(uncertainity)
    pi_line.append(math.pi/4)

plt.semilogx(mean_line,uncertainity_line)
plt.hlines(math.pi/4,xmin=0,xmax=18446744073709551616)
plt.savefig('Ex2.png')