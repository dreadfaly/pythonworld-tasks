# Времена года (4)
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, 
# которому этот месяц принадлежит (зима, весна, лето или осень).

def season(x):
	if x == 1 or x == 2 or x == 12:
		return 'Winter'
	elif x == 3 or x == 4 or x == 5:
		return 'Spring'
	elif x == 6 or x == 7 or x == 8:
		return 'Summer'
	elif x == 9 or x == 10 or x == 11:
		return 'Autumn'
	else:
		return 'Unknown operation'
