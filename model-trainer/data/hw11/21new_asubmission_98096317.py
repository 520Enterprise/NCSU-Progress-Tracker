import numpy as np
#@#
def pair_max(arr1,arr2):
#@#
	l = []
	for i,c in zip(arr1,arr2):
#@#
		l.append(max(i,c))
#@#
	apair = np.array(l)
	return apair
#@#
def main():
if __name__ == '__main__':
    main()
#@#