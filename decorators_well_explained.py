# codes with decorators


import time 

def time_it(func):
	def wrapper(*args,**kwargs):
		start = time.time()
		result = func(*args,**kwargs)
		end = time.time()
		print (func.__name__ + " took " + str((end-start)*1000) + " milli second")

		return result
	return wrapper

@time_it
def square(number):
	result = []
	for i in number:
		result.append(i*i)

	return result

@time_it
def cube(number):
	result = []

	for i in number:
		result.append(i*i*i)
	return result


array = range(1,1000)
square(array)
cube(array)





