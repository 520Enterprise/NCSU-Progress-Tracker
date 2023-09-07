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
            point = 2
            testdata = np.loadtxt(filename, skiprows = 1, delimiter = ',', usecols = [2])
            timedata = np.loadtxt(filename, skiprows = 1, delimiter = ',', usecols = [5])
            while i < len(stats):
                if stats[i] == 'mean':
                    plt.plot(point, np.mean(testdata), 'rs')
                    plt.plot(point, np.mean(timedata), 'cs')
                elif stats[i] == 'median':
                    plt.plot(point, np.median(testdata), 'ro')
                    plt.plot(point, np.median(timedata), 'co')
                elif stats[i] == 'std_dev':
                    plt.plot(point, np.std(testdata), 'r*')
                    plt.plot(point, np.std(timedata), 'c*')
                i += 1
        elif tests[n] == 3:
            point = 3
            testdata = np.loadtxt(filename, skiprows = 1, delimiter = ',', usecols = [3])
            timedata = np.loadtxt(filename, skiprows = 1, delimiter = ',', usecols = [6])
            while i < len(stats):
                if stats[i] == 'mean':
                    plt.plot(point, np.mean(testdata), 'ks')
                    plt.plot(point, np.mean(timedata), 'gs')
                elif stats[i] == 'median':
                    plt.plot(point, np.median(testdata), 'ko')
                    plt.plot(point, np.median(timedata), 'go')
                elif stats[i] == 'std_dev':
                    plt.plot(point, np.std(testdata), 'k*')
                    plt.plot(point, np.std(timedata), 'g*')
                i += 1
        n += 1
    return plt.show
def main():
    plot_stats_for_test('grades_times.csv',[1,3],['mean'])
if __name__ == '__main__':
    main()
