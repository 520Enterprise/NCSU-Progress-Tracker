import matplotlib.pyplot as plt
import numpy as np
def plot_stats_for_test(filename, tests, stats):
    for stats in stats:
        for i in tests:
            y_test_vals = np.loadtxt(filename, usecols=[i], delimiter=',', skiprows=1)
            if i == 1:
                if stats == 'mean':
                    y_test_vals = np.mean(y_test_vals)
                    x_vals = i
                    plt.plot(x_vals,y_test_vals, 'bs')
                elif stats == 'median':
                    y_test_vals = np.median(y_test_vals)
                    x_vals = i
                    plt.plot(x_vals,y_test_vals, 'bo')
                elif stats == 'std_dev':
                    y_test_vals = np.std(y_test_vals)
                    x_vals = i
                    plt.plot(x_vals,y_test_vals, 'b*')
            if i == 2:
                if stats == 'mean':
                    y_test_vals = np.mean(y_test_vals)
                    x_vals = i
                    plt.plot(x_vals,y_test_vals, 'rs')
                elif stats == 'median':
                    y_test_vals = np.median(y_test_vals)
                    x_vals = i
                    plt.plot(x_vals,y_test_vals, 'ro')
                elif stats == 'std_dev':
                    y_test_vals = np.std(y_test_vals)
                    x_vals = i
                    plt.plot(x_vals,y_test_vals, 'r*')
            if i == 3:
