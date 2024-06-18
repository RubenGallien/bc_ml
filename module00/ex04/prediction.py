import numpy as np

def add_intercept(x):
	if not isinstance(x, np.ndarray):
		raise TypeError("x is not a np.ndarray")
	if len(x) == 0:
		raise ValueError("Empty array")
	x = x.reshape(-1, 1)
	new_col = np.ones((x.shape[0], 1))
	return np.hstack((new_col, x))

def predict_(x, theta):
	if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
		return None
	if x.ndim != 1:
		return None
	if theta.ndim != 2:
		return None
	new_x = add_intercept(x)
	return np.dot(new_x, theta)
