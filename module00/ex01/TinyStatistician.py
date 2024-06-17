import numpy as np
import math

class TinyStatistician:
	def __init__(self) -> None:
		pass

	def mean(self, x):
		if not isinstance(x, (list, np.ndarray)):
			return None
		if len(x) == 0:
			return None
		total = 0.0
		for i in x:
			total += i
		total = total / len(x)
		return total

	def median(self, x):
		if not isinstance(x, (list, np.ndarray)):
			return None
		if len(x) == 0:
			return None
		x = sorted(x)
		n = len(x)
		mid = n // 2
		if n % 2 == 1:
			return float(x[mid])
		else:
			return (x[mid - 1] + x[mid]) / 2.0

	def closest(nb):
		integer = math.floor(nb)
		decimal = nb - integer
		if decimal < 0.51:
			return integer
		else:
			return integer + 1

	def quartile(self, x):
		if not isinstance(x, (list, np.ndarray)):
			return None
		if len(x) == 0:
			return None
		lst = []
		x = sorted(x)
		Q1 = (1 / 4) * len(x)
		Q3 = (3 / 4) * len(x)
		lst.append(x[TinyStatistician.closest(Q1)])
		lst.append(x[TinyStatistician.closest(Q3)])
		return lst

	def percentile(self, x, p):
		if not isinstance(x, (list, np.ndarray)):
			return None
		if len(x) == 0:
			return None
		x = sorted(x)
		frac = (p / 100) * (len(x) - 1)
		result = x[math.floor(frac)] + ((frac % 1) * x[math.floor(frac) + 1] - (frac % 1) * x[math.floor(frac)])
		print(result)

	def var(self, x):
		x = sorted(x)
		total = 0.0
		for i in x:
			total += i;
		moyenne = total / len(x)
		ecart = 0.0
		for i in x:
			ecart += round((i - moyenne) * (i - moyenne));
		var = ecart / (len(x) - 1)
		return var

	def std(self, x):
		return (math.sqrt(TinyStatistician.var(self, x)))