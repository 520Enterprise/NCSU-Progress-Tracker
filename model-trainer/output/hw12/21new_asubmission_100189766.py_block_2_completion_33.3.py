import matplotlib.pyplot as plt
import numpy as np
import statistics
def plot_stats_for_test(filename, tests, stats):
    data = np.loadtxt(filename, usecols=[1,2,3,4,5,6], delimiter=',', skiprows=1)
    test1 = []
    test2 = []
    test3 = []
    time1 = []
    time2 = []
    time3 = []
    for line in range(len(data)):
        test1.append(data[line, 0])
        test2.append(data[line, 1])
        test3.append(data[line, 2])
        time1.append(data[line, 3])
        time2.append(data[line, 4])
        time3.append(data[line, 5])
    if stats == ['mean']:
