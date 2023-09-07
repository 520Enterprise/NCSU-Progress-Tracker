import numpy as np
import matplotlib.pyplot as plt
def plot_stats_for_test(filename, tests, stats):
    testtype = {1:['b','y'], 2:['r','c'], 3:['k','g']}
    for a in range(len(tests)):
        file = np.loadtxt(filename, skiprows=1, usecols=[tests[a],(tests[a]+3)], delimiter =',')
        grade = []
        time = []
        for b in range(len(file)):
            grade += [file[b][0]]
            time += [file[b][1]]
        garr = np.array(grade)
        tarr = np.array(time)
        stattype = {"mean":[np.mean(garr), 's', np.mean(tarr)], 
                        "median":[np.median(garr), 'o', np.median(tarr)], 
                        "std_dev":[np.std(garr), '*', np.std(tarr)]}
        for c in stats:
