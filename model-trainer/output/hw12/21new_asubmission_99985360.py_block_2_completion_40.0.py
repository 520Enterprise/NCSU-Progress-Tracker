import numpy as np
import matplotlib.pyplot as plt
def plot_stats_for_test(filename, tests, stats):
    testtype = {1:['b','y'], 2:['r','c'], 3:['k','g']}
    for a in range(len(tests)):
