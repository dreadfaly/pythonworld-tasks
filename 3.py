# Квадрат (3)
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью 
# кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side):
	d = side * 1,41421356237
	return (side*4, side*side, d)
