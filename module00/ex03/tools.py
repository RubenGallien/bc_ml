import numpy as np

def add_intercept(x):
	if not isinstance(x, np.ndarray):
		raise TypeError("x is not a np.ndarray")
	if len(x) == 0:
		raise ValueError("Empty array")
	x = x.reshape(-1, 1)
	new_col = np.ones((x.shape[0], 1))
	return np.hstack((new_col, x))
