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
        if tests == [1,3]:
            te1 = sum(test1) / len(test1)
            te3 = sum(test3) / len(test3)
            ti1 = sum(time1) / len(time1)
            ti3 = sum(time3) / len(time3)           
            plt.plot(1, ti1, 'ys')
            plt.plot(3, ti3, 'gs')
            plt.plot(1, te1, 'bs')
            plt.plot(3, te3, 'ks')
        elif tests == [1,2]:
            te1 = sum(test1) / len(test1)
            te2 = sum(test2) / len(test2)
            ti1 = sum(time1) / len(time1)
            ti2 = sum(time2) / len(time2)           
            plt.plot(1, ti1, 'ys')
            plt.plot(2, ti2, 'cs')
            plt.plot(1, te1, 'bs')
            plt.plot(2, te2, 'rs')
        elif tests == [2,3]:
            te2 = sum(test2) / len(test2)
            te3 = sum(test3) / len(test3)
            ti2 = sum(time2) / len(time2)
            ti3 = sum(time3) / len(time3)           
            plt.plot(2, ti2, 'cs')
            plt.plot(3, ti3, 'gs')
            plt.plot(2, te2, 'rs')
            plt.plot(3, te3, 'ks')
        elif tests == [1,2,3]:
            te1 = sum(test1) / len(test1)
            te2 = sum(test2) / len(test2)
            te3 = sum(test3) / len(test3)
            ti1 = sum(time1) / len(time1)
            ti2 = sum(time2) / len(time2)
            ti3 = sum(time3) / len(time3)           
            plt.plot(1, ti1, 'ys')
            plt.plot(2, ti2, 'cs')
            plt.plot(3, ti3, 'gs')
            plt.plot(1, te1, 'bs')
            plt.plot(3, te3, 'ks')
            plt.plot(2, te2, 'rs')
    elif stats == ['median']:
