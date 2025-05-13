import random

numbers = "0, 1, 2, 3, 4, 5, 6, 7"
numbers = numbers.replace(" ", "")
numbers = numbers.split(",")
try:
	numbers = [int(number) for number in numbers]
	print(numbers)
	random_number = random.choice(numbers)
	print(random_number)
except ValueError:
	print("Ошибка приведения типов")