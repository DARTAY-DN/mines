import time, random, os

score = 0
score_not = True

while score_not:
	print('''\033[34mChoose the desired cell

	[ 1 ] [ 2 ] [ 3 ]
	[ 4 ] [ 5 ] [ 6 ]
	[ 7 ] [ 8 ] [ 9 ]''')
	try:
			result = int(input('-> '))
			if result >= 9:
				print('The odds are only 1 to 9!')
				score_not = False
				score -= 9999999
			if result <= 1:
				print('The odds are only 1 to 9!')
				score_not = False
				score -= 9999999
			resone = random.choice(['Верно', 'Неверно'])
			if resone == 'Верно':
				print('You Win')
				score += 3
				time.sleep(3)
				print('By you ' + str(score) + ' points')
				time.sleep(1.5)
				os.system('clear')
			else:
				print('You Lose')
				score -= 3
				time.sleep(3)
				print('By one ' + str(score) + ' points')
				time.sleep(1.5)
				os.system('clear')
				if score <= -1:
					score_not = False
					print('You have no points left, Restart the game!')
					if score == 12:
						name = input('You Won, what is your name as a winner? ')
						time.sleep(1)
						print('Thanks for the game, ' +  str(name))
						score_not = False
			
	except ValueError:
		print('Need to enter numbers!!!')
					
						
			
