import numpy as np

def simple_predict(x, theta):
	if not isinstance(x, np.ndarray):
		raise TypeError("argument is not a numpy.ndarray")
	if not isinstance(theta, np.ndarray):
		raise TypeError("argument is not a numpy.ndarry")
	