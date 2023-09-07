import matplotlib.pyplot as plt
import numpy as np
def plot_stats_for_test(filename, tests, stats):
    data = np.loadtxt(filename, usecols=[1,2,3,4,5,6], delimiter = ',', skiprows=1)
    for element in stats:
        if element == 'mean':
            mean_test_1 = np.array([])
            mean_test_2 = np.array([])
            mean_test_3 = np.array([])
            mean_study_1 = np.array([])
            mean_study_2 = np.array([])
            mean_study_3 = np.array([])
            test_grade_mean = np.array([])
            study_time_mean = np.array([])
            for num in tests:
                if num == 1:
                    for line in data:
                        mean_test_1 = np.append(mean_test_1, line[0])
                        mean_study_1 = np.append(mean_study_1, line[3])
                    test_grade_mean = np.mean(mean_test_1)
                    study_time_mean = np.mean(mean_study_1)
                    plt.plot(num, test_grade_mean, 'bs')
                    plt.plot(num, study_time_mean, 'ys')
                elif num == 2:
                    for line in data:
                        mean_test_2 = np.append(mean_test_2, line[1])
                        mean_study_2 = np.append(mean_study_2, line[4])
                    test_grade_mean = np.mean(mean_test_2)
                    study_time_mean = np.mean(mean_study_2)
                    plt.plot(num, test_grade_mean, 'rs')
                    plt.plot(num, study_time_mean, 'cs')
                elif num == 3:
                    for line in data:
                        mean_test_3 = np.append(mean_test_3, line[2])
                        mean_study_3 = np.append(mean_study_3, line[5])
                    test_grade_mean = np.mean(mean_test_3)
                    study_time_mean = np.mean(mean_study_3)
                    plt.plot(num, test_grade_mean, 'ks')
                    plt.plot(num, study_time_mean, 'gs')
        elif element == 'median':
            median_test_1 = np.array([])
            median_test_2 = np.array([])
            median_test_3 = np.array([])
            median_study_1 = np.array([])
            median_study_2 = np.array([])
            median_study_3 = np.array([])
            test_grade_median = np.array([])
            study_time_median = np.array([])
            for num in tests:
                if num == 1:
                    for line in data:
                        median_test_1 = np.append(median_test_1, line[0])
                        median_study_1 = np.append(median_study_1, line[3])
                    test_grade_median = np.median(median_test_1)
                    study_time_median = np.median(median_study_1)
                    plt.plot(num, test_grade_median, 'bo')
                    plt.plot(num, study_time_median, 'yo')
                elif num == 2:
                    for line in data:
                        median_test_2 = np.append(median_test_2, line[1])
                        median_study_2 = np.append(median_study_2, line[4])
                    test_grade_median = np.median(median_test_2)
                    study_time_median = np.median(median_study_2)
                    plt.plot(num, test_grade_median, 'ro')
                    plt.plot(num, study_time_median, 'co')
                elif num == 3:
                    for line in data:
                        median_test_3 = np.append(median_test_3, line[2])
                        median_study_3 = np.append(median_study_3, line[5])
                    test_grade_median = np.median(median_test_3)
                    study_time_median = np.median(median_study_3)
                    plt.plot(num, test_grade_median, 'ko')
                    plt.plot(num, study_time_median, 'go')
        elif element == 'std_dev':
            std_dev_test_1 = np.array([])
            std_dev_test_2 = np.array([])
            std_dev_test_3 = np.array([])
            std_dev_study_1 = np.array([])
            std_dev_study_2 = np.array([])
            std_dev_study_3 = np.array([])
            test_grade_std_dev = np.array([])
            study_time_std_dev = np.array([])
            for num in tests:
                if num == 1:
                    for line in data:
                        std_dev_test_1 = np.append(std_dev_test_1, line[0])
                        std_dev_study_1 = np.append(std_dev_study_1, line[3])
                    test_grade_std_dev = np.std(std_dev_test_1)
                    study_time_std_dev = np.std(std_dev_study_1)
                    plt.plot(num, test_grade_std_dev, 'b*')
                    plt.plot(num, study_time_std_dev, 'y*')
                elif num == 2:
                    for line in data:
                        std_dev_test_2 = np.append(std_dev_test_2, line[1])
                        std_dev_study_2 = np.append(std_dev_study_2, line[4])
                    test_grade_std_dev = np.std(std_dev_test_2)
                    study_time_std_dev = np.std(std_dev_study_2)
                    plt.plot(num, test_grade_std_dev, 'r*')
                    plt.plot(num, study_time_std_dev, 'c*')
                elif num == 3:
                    for line in data:
                        std_dev_test_3 = np.append(std_dev_test_3, line[2])
                        std_dev_study_3 = np.append(std_dev_study_3, line[5])
                    test_grade_std_dev = np.std(std_dev_test_3)
                    study_time_std_dev = np.std(std_dev_study_3)
                    plt.plot(num, test_grade_std_dev, 'k*')
                    plt.plot(num, study_time_std_dev, 'g*')
def main():
    plot_stats_for_test('grades_times.csv',[1,3],['mean'])
    plt.show()
    plot_stats_for_test('grades_times.csv', [1,2,3], ['mean','median', 'std_dev'])
    plt.show()
    plot_stats_for_test('grades_times.csv', [2,3], ['median', 'std_dev'])
    plt.show()
if __name__ == '__main__':
    main()
