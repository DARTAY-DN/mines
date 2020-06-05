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
		if result >= 9:
			print('Шансы только от 1 до 9!')
			score_not = False
			score -= 9999999
		if result <= 1:
			print('Шансы только от 1 до 9!')
			score_not = False
			score -= 9999999
		resone = random.choice(['Верно', 'Неверно'])
		if resone == 'Верно':
			print('You Win')
			score += 3
			time.sleep(3)
			print('У тебя ' + str(score) + ' Очка/ов')
			time.sleep(1.5)
			os.system('clear')
		else:
			print('You Lose')
			score -= 3
			time.sleep(3)
			print('У тебя ' + str(score) + ' Очка/ов')
			time.sleep(1.5)
			os.system('clear')
			if score <= -1:
				score_not = False
				print('У тебя не осталось очков,Перезапусти игру!')
		if score == 12:
			name = input('Ты Победил, как тебя звать победитель? ')
			time.sleep(1)
			print('Спасибо за игру, ' +  str(name))
			score_not = False
	
	except ValueError:
		print('Нужно вводить числа!!!')
