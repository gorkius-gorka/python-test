import random

numbers_str = "0, 1, 2, 3, 4, 5, 6, 7"
numbers_str = numbers_str.replace(" ", "")
numbers_str = numbers_str.split(",")
try:
	numbers = [int(number) for number in numbers_str]
	print(numbers)
	random_number = random.choice(numbers)
	print(random_number)
except ValueError:
	print("Ошибка приведения типов")