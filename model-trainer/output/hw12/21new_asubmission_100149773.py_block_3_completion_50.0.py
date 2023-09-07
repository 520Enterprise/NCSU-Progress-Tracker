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
                plt.plot(element, np.mean(grade_data),color=grade_color[element-1], marker='s')
                fileus.seek(0)
                plt.plot(element, np.mean(time_data),color=time_color[element-1], marker='s')
                fileus.seek(0)
            if 'median' in stats:
