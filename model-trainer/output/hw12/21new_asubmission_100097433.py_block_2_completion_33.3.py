import numpy as np
import matplotlib.pyplot as plt
def plot_stats_for_test(filename, tests, stats):
    grades = []
    grade_mean = []
    grade_median = []
    grade_std = []
    times = []
    time_mean = []
    time_median = []
    time_std = []
    for i in [1,2,3]:
        grades.append(np.loadtxt(filename, usecols=i, delimiter = ',', skiprows=1))
        grade_mean.append(np.mean(grades))
        grade_median.append(np.median(grades))
        grade_std.append(np.std(grades))
        grades = []
    for i in [4,5,6]:
        times.append(np.loadtxt(filename, usecols=i, delimiter = ',', skiprows=1))
        time_mean.append(np.mean(times))
        time_median.append(np.median(times))
        time_std.append(np.std(times))
        times = []
    grade_dots = ['b','r','k']
    time_dots = ['y','c','g'] 
    if 'mean' in stats:
