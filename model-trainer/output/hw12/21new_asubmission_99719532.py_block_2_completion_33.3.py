import numpy as np 
import matplotlib.pyplot as plt
def plot_stats_for_tests(filename,tests,stats):
    for function in stats: 
        if function == 'mean':
