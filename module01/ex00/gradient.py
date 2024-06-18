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
	ret = np.zeros((2, 1), float)
	for i in range(len(x)):
		y_hat = theta[0] + theta[1] * x[i]
		diff = y_hat - y[i]
		ret[0] += diff
		ret[1] += diff * x[i]
	ret[0] = ret[0] / len(x)
	ret[1] = ret[1] / len(x)
	return ret


x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))

theta1 = np.array([2, 0.7]).reshape((-1, 1))

print(simple_gradient(x, y, theta1))