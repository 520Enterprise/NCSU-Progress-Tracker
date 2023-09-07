import numpy as np 
import matplotlib.pyplot as plt
def plot_stats_for_tests(filename,tests,stats):
    for function in stats: 
        if function == 'mean':
            for numbers in tests: 
                if numbers == 1:
                    scores = np.loadtxt(filename, delimiter = ',', usecols=[1],skiprows =1)
                    times = np.loadtxt(filename, delimiter = ',', usecols=[4],skiprows =1)
                    scores_mean = np.mean(scores)
                    times_mean = np.mean(times)
                    plt.plot(1,scores_mean,'bs')
                    plt.plot(1,times_mean,'ys')
                elif numbers == 2: 
                    scores = np.loadtxt(filename, delimiter = ',', usecols=[2],skiprows =1)
                    times = np.loadtxt(filename, delimiter = ',', usecols=[5],skiprows =1)
                    scores_mean = np.mean(scores)
                    times_mean = np.mean(times)
                    plt.plot(2,scores_mean,'rs')
                    plt.plot(2,times_mean,'cs')
                elif numbers == 3: 
                    scores = np.loadtxt(filename, delimiter = ',', usecols=[3],skiprows =1)
                    times = np.loadtxt(filename, delimiter = ',', usecols=[6],skiprows =1)
                    scores_mean = np.mean(scores)
                    times_mean = np.mean(times)
                    plt.plot(3,scores_mean,'ks')
                    plt.plot(3,times_mean,'gs')
        elif function == 'median': 
            for number in tests: 
                if number == 1:
                    scores = np.loadtxt(filename, delimiter = ',', usecols=[1],skiprows =1)
                    times = np.loadtxt(filename, delimiter = ',', usecols=[4],skiprows =1)
                    scores_median = np.median(scores)
                    times_median = np.median(times)
                    plt.plot(1,scores_median,'bo')
                    plt.plot(1,times_median,'yo')
                elif number == 2: 
                    scores = np.loadtxt(filename, delimiter = ',', usecols=[2],skiprows =1)
                    times = np.loadtxt(filename, delimiter = ',', usecols=[5],skiprows =1)
                    scores_median = np.median(scores)
                    times_median = np.median(times)
                    plt.plot(2,scores_median,'ro')
                    plt.plot(2,times_median,'co')
                elif number == 3: 
                    scores = np.loadtxt(filename, delimiter = ',', usecols=[3],skiprows =1)
                    times = np.loadtxt(filename, delimiter = ',', usecols=[6],skiprows =1)
                    scores_median = np.median(scores)
                    times_median = np.median(times)
                    plt.plot(3,scores_median,'ko')
                    plt.plot(3,times_median,'go')
        elif function == 'std_dev':
            for number in tests: 
                if number == 1:
                    scores = np.loadtxt(filename, delimiter = ',', usecols=[1],skiprows =1)
                    times = np.loadtxt(filename, delimiter = ',', usecols=[4],skiprows =1)
                    scores_std = np.std(scores)
                    times_std = np.std(times)
                    plt.plot(1,scores_std,'b*')
                    plt.plot(1,times_std,'y*')
                elif number == 2: 
                    scores = np.loadtxt(filename, delimiter = ',', usecols=[2],skiprows =1)
                    times = np.loadtxt(filename, delimiter = ',', usecols=[5],skiprows =1)
                    scores_std = np.std(scores)
                    times_std = np.std(times)
                    plt.plot(2,scores_std,'r*')
                    plt.plot(2,times_std,'c*')
                elif number == 3: 
                    scores = np.loadtxt(filename, delimiter = ',', usecols=[3],skiprows =1)
                    times = np.loadtxt(filename, delimiter = ',', usecols=[6],skiprows =1)
                    scores_std = np.std(scores)
                    times_std = np.std(times)
                    plt.plot(3,scores_std,'k*')
                    plt.plot(3,times_std,'g*')
    plt.show()
