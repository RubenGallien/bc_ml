import numpy as np

def simple_gradient(x, y, theta):
	if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
		return None
	if not x.shape == (x.shape[0], 1) and x.shape[0] > 0:
		return None
	if not y.shape == (y.shape[0], 1) and y.shape[0] > 0:
		return None
	if not theta.shape == (2, 1):
		return None
	print(x)
	add_col = np.ones((x.shape[0], 1))
	print(add_col)
	new_x = np.hstack((add_col, x))
	print(new_x)
	res = (new_x @ theta) - y
	print(res)
	return (new_x.T @ res) / len(y)


x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))
# Example 0:
theta1 = np.array([2, 0.7]).reshape((-1, 1))
print(simple_gradient(x, y, theta1))