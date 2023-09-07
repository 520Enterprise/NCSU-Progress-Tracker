import numpy as np
def pair_max(arr1,arr2):
	l = []
	for i,c in zip(arr1,arr2):
		l.append(max(i,c))
