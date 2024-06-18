import numpy as np

def simple_predict(x, theta):
	d_list = []
	if not isinstance(x, np.ndarray):
		raise TypeError("argument is not a numpy.ndarray")
	if not isinstance(theta, np.ndarray):
		raise TypeError("argument is not a numpy.ndarry")
	for i in x:
		d_list.append((theta[1] * i) + theta[0])
		ret = np.array(d_list, float)
	return ret