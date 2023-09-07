import numpy as np
import matplotlib.pyplot as plt
def plot_stats_for_test(filename, tests, stats):
    n = 0
    while n < len(tests):
        i = 0
        if tests[n] == 1:
            point = 1
            testdata = np.loadtxt(filename, skiprows = 1, delimiter = ',', usecols = [1])
            timedata = np.loadtxt(filename, skiprows = 1, delimiter = ',', usecols = [4])
            while i < len(stats):
                if stats[i] == 'mean':
                    plt.plot(point, np.mean(testdata), 'bs')
                    plt.plot(point, np.mean(timedata), 'ys')
                elif stats[i] == 'median':
                    plt.plot(point, np.median(testdata), 'bo')
                    plt.plot(point, np.median(timedata), 'yo')
                elif stats[i] == 'std_dev':
                    plt.plot(point, np.std(testdata), 'b*')
                    plt.plot(point, np.std(timedata), 'y*')
                i += 1
        elif tests[n] == 2:
