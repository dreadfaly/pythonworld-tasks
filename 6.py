# Простые числа (6)
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

def is_prime(x):
	range_max = 10000
	max_list = [1]

	for y in range (range_max):
		if y == 0 or y == x:
			y += 1
		else:
			z = x / y
			if z > int(z):
				max_list.append(0)
			else:
				max_list.append(1)

	if max_list.count(1) <= 2:
		if x == 1:
			return False
		else:
			return True
	else:
		return False
