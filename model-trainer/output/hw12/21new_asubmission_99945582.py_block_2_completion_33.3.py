import numpy as np
import matplotlib.pyplot as plt
def plot_stats_for_test(filename, tests, stats):
    n = 0
    while n < len(tests):
        i = 0
        if tests[n] == 1:
