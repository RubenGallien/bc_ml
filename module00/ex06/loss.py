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
		return ("1")
	if theta.ndim != 2:
		return ("3")
	new_x = add_intercept(x)
	return np.dot(new_x, theta)

def loss_elem_(y1, y_hat):
	if not isinstance(y1, np.ndarray) or not isinstance(y_hat, np.ndarray):
		return None
	if y1.ndim != 2 or y_hat.ndim != 2:
		return None
	ret = []
	ind = 0
	for i in y1:
		value = (i - y_hat[ind]) * (i - y_hat[ind])
		ret.append(value)
		ind += 1
	ret_np = np.array(ret)
	return ret_np

def loss_(y1, y_hat1):
	diff = loss_elem_(y1, y_hat1)
	moyenne = sum(diff)
	moyenne = moyenne / (2 * len(y1))
	return moyenne[0]

x2 = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(-1, 1)
theta2 = np.array(np.array([[0.], [1.]]))
y_hat2 = predict_(x2, theta2)
y2 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)
# Example 3:
print(loss_(y2, y_hat2))