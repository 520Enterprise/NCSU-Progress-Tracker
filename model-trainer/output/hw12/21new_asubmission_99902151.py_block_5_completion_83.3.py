import numpy as np
import matplotlib.pyplot as plt
def plot_stats_for_test(filename,tests,stats):
    data_test_1 = np.loadtxt(filename, usecols=1, delimiter=',',skiprows=1) 
    data_test_2 = np.loadtxt(filename, usecols=2, delimiter=',',skiprows=1)
    data_test_3 = np.loadtxt(filename, usecols=3, delimiter=',',skiprows=1)
    data_times_1 = np.loadtxt(filename, usecols=4, delimiter=',',skiprows=1)
    data_times_2 = np.loadtxt(filename, usecols=5, delimiter=',',skiprows=1)
    data_times_3 = np.loadtxt(filename, usecols=6, delimiter=',',skiprows=1)
    test_grades =[data_test_1, data_test_2, data_test_3]
    test_times=[data_times_1, data_times_2, data_times_3]
    test_colors = ["b","r","k"]
    time_colors = ["y","c","g"]
    plt.xlabel("Tests")
    plt.ylabel(stats)
    plt.title("Stats for Test")
    for stat in stats:
            for test in tests:
                if stat == "median":
                    plt.plot(test,np.median(np.array(test_grades[test - 1])),test_colors[test-1]+"o")
                    plt.plot(test,np.median(np.array(test_times[test - 1])),time_colors[test-1]+"o")
                elif stat == "mean":
                    plt.plot(test,np.mean(np.array(test_grades[test - 1])),test_colors[test-1]+"s")
                    plt.plot(test,np.mean(np.array(test_times[test - 1])),time_colors[test-1]+"s")
                elif stat == "std_dev":
                    plt.plot(test,np.std(np.array(test_grades[test - 1])),test_colors[test-1]+"*")
                    plt.plot(test,np.std(np.array(test_times[test - 1])),time_colors[test-1]+"*")
    plt.show() 
