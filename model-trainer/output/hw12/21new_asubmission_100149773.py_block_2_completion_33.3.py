import numpy as np
import matplotlib.pyplot as plt
def plot_stats_for_test(filename, tests, stats):
    grade_data=[]
    time_data=[]
    grade_color=['b','r','k']
    time_color=['y','c','g']
    with open(filename, 'r') as fileus:
        for element in tests:
            grade_data=np.loadtxt(fileus, usecols=[element], skiprows=1, delimiter=',')
            fileus.seek(0)
            time_data=np.loadtxt(fileus, usecols=[element+3], skiprows=1, delimiter=',')
            if 'mean' in stats:
