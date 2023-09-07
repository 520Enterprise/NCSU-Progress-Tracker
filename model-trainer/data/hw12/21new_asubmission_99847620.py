import matplotlib.pyplot as plt
import numpy as np
#@#
def plot_stats_for_test(filename, tests, stats):
    for item in stats:
        if item == "mean":
#@#
            for items in tests:
                if items == 1:
                    data_grades = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [1])
                    data_times = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [4])
                    mean = np.mean(data_times)
                    mean1 = np.mean(data_grades)
                    plt.plot([1], [mean], 'ys')
                    plt.plot([1], [mean1], 'bs')
                elif items == 2:
                    data_grades = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [2])
                    data_times = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [5])
                    mean = np.mean(data_times)
                    mean1 = np.mean(data_grades)
                    plt.plot([2], [mean], 'cs')
                    plt.plot([2], [mean1], 'rs')
                elif items == 3:
                    data_grades = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [3])
                    data_times = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [6])
                    mean = np.mean(data_times)
                    mean1 = np.mean(data_grades)
                    plt.plot([3], [mean], 'gs')
                    plt.plot([3], [mean1], 'ks')
        elif item == "median":
#@#
            for items in tests:
                if items == 1:
                    data_grades = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [1])
                    data_times = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [4])
                    median = np.median(data_times)
                    median1 = np.median(data_grades)
                    plt.plot([1], [median], 'yo')
                    plt.plot([1], [median1], 'bo')
                elif items == 2:
                    data_grades = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [2])
                    data_times = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [5])
                    median = np.median(data_times)
                    median1 = np.median(data_grades)
                    plt.plot([2], [median], 'co')
                    plt.plot([2], [median1], 'ro')
                elif items == 3:
                    data_grades = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [3])
                    data_times = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [6])
                    median = np.median(data_times)
                    median1 = np.median(data_grades)
                    plt.plot([3], [median], 'go')
                    plt.plot([3], [median1], 'ko')
        elif item == "std_dev":
#@#
            for items in tests:
                if items == 1:
                    data_grades = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [1])
                    data_times = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [4])
                    stddev = np.std(data_times)
                    stddev1 = np.std(data_grades)
                    plt.plot([1], [stddev], 'y*')
                    plt.plot([1], [stddev1], 'b*')
                elif items == 2:
                    data_grades = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [2])
                    data_times = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [5])
                    stddev = np.std(data_times)
                    stddev1 = np.std(data_grades)
                    plt.plot([2], [stddev], 'c*')
                    plt.plot([2], [stddev1], 'r*')
                elif items == 3:
                    data_grades = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [3])
                    data_times = np.loadtxt(filename, skiprows=1, delimiter = ",", usecols= [6])
                    stddev = np.std(data_times)
                    stddev1 = np.std(data_grades)
                    plt.plot([3], [stddev], 'g*')
                    plt.plot([3], [stddev1], 'k*')
    return plt.show()
#@#
def main():
    plot_stats_for_test('grades_times.csv',[1,3],['mean'])
    plot_stats_for_test('grades_times.csv', [1,2,3], ['mean', 'median', 'std_dev'])
if __name__ == '__main__':
    main()
#@#