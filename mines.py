import random
import time
import os

#Переменные
score_not = True
score = 0

while score_not:
	print('''\033[34mВыбери нужную ячейку
	[ 1 ] [ 2 ] [ 3 ]
	[ 4 ] [ 5 ] [ 6 ]
	[ 7 ] [ 8 ] [ 9 ]''')
	try:
		result = int(input('-> '))
		resone = random.choice(['Верно', 'Неверно'])
		if resone == 'Верно':
			print('Win')
			score += 3
			time.sleep(3)
			print('У тебя ' + str(score) + ' Очка/ов')
			time.sleep(1.5)
			os.system('clear')
		else:
			print('Lose')
			score -= 3
			time.sleep(3)
			print('У тебя ' + str(score) + ' Очка/ов')
			time.sleep(1.5)
			os.system('clear')
			if score <= 0:
				score_not = False
				print('У тебя не осталось очков,Перезапусти игру!')
	except ValueError:
		print('Нужно вводить числа!!!')
