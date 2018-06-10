# Високосный год (2)
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def is_year_leap(year):
	return not year / 4 > int(year/4)
