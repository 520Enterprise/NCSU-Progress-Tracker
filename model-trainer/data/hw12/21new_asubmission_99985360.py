import numpy as np
import matplotlib.pyplot as plt
#@#
def plot_stats_for_test(filename, tests, stats):
    testtype = {1:['b','y'], 2:['r','c'], 3:['k','g']}
    for a in range(len(tests)):
#@#
        file = np.loadtxt(filename, skiprows=1, usecols=[tests[a],(tests[a]+3)], delimiter =',')
        grade = []
        time = []
        for b in range(len(file)):
#@#
            grade += [file[b][0]]
            time += [file[b][1]]
        garr = np.array(grade)
        tarr = np.array(time)
        stattype = {"mean":[np.mean(garr), 's', np.mean(tarr)], 
                        "median":[np.median(garr), 'o', np.median(tarr)], 
                        "std_dev":[np.std(garr), '*', np.std(tarr)]}
        for c in stats:
#@#
            garr = stattype[c][0]
            color = testtype[tests[a]][0] + stattype[c][1]
            plt.plot(tests[a], garr, color)
            tarr = stattype[c][2]
            color = testtype[tests[a]][1] + stattype[c][1]
            plt.plot(tests[a], tarr, color)
    plt.show()
#@#
def main():
    plot_stats_for_test('grades_times.csv',[1,3],['mean'])
    plot_stats_for_test('grades_times.csv', [1,2,3], ['mean', 'median', 'std_dev'])
    plot_stats_for_test('grades_times.csv', [2,3], ['median', 'std_dev'])
if __name__ == '__main__':
    main()
#@#