import matplotlib.pyplot as plt
import numpy as np
def plot_stats_for_test(filename, tests, stats):
    for item in stats:
        if item == "mean":
