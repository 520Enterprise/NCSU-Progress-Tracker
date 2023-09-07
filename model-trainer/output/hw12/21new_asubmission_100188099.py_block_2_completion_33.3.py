import matplotlib.pyplot as plt
import numpy as np
def plot_stats_for_test(filename, tests, stats):
    for stats in stats:
        for i in tests:
            y_test_vals = np.loadtxt(filename, usecols=[i], delimiter=',', skiprows=1)
            if i == 1:
