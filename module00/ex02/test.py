import numpy as np
from predictions import simple_predict

x = np.arange(1, 6)
theta2 = np.array([-3, 1])
print(simple_predict(x, theta2))