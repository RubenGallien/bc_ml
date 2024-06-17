class Matrix:
	def __init__(self, lst):
		if isinstance(lst, tuple):
			mat = []
			for i in range(lst[0]):
				row_list = []
				for j in range(lst[1]):
					row_list.append(0)
				mat.append(row_list)
			self.shape = (lst[0], lst[1])
			self.data = mat
		else:
			self.shape = (len(lst), len(lst[0]))
			self.data = lst

	def __add__(self, other):
		if not isinstance(other, Matrix):
			raise TypeError("Need Matrix")
		if self.shape != other.shape:
			raise ValueError("Addition is only possible with matrices with the same shape")
		return Matrix([[a + b for a, b in zip(x, y)]
        for x, y in zip(self.data, other.data)])

	def __sub__(self, other):
		if not isinstance(other, Matrix):
			raise TypeError("Need Matrix")
		if self.shape != other.shape:
			raise ValueError("Substraction is only possible with matrices with the same shape")
		return Matrix([[a - b for a, b in zip(x, y)]
        for x, y in zip(self.data, other.data)])

	def __truediv__(self, other):
		if not isinstance(other, (int, float)):
			raise TypeError("Need Matrix")
		return Matrix([[a / other for a in x]
						for x in self.data])

	def mul(self, arg):
		if isinstance(arg, Matrix):
			data = []
			for i in range(self.shape[0]):
				row = []
				for j in range(arg.shape[1]):
					val = 0
					for k in range(self.shape[1]):
						val += self.data[i][k] * arg.data[k][j]
					row.append(val)
				data.append(row)
			return Matrix(data)
		elif isinstance(arg, int):
			print("ok")

	def __rtruediv__(self, other):
		raise TypeError("impossible i")

	def __rsub__(self, other):
		return self.__sub__(other)

	def __radd__(self, other):
		return self.__add__(other)

	def __str__(self):
		ret = type(self).__name__ + "(\n"
		for row in self.data:
			ret += " " + str(row) + "\n"
		ret += ")"
		return ret