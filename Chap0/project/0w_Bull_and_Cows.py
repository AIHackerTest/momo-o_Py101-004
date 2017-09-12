import random
from sys import exit

print('''Get ready to start Bull and Cows? 
Please press [enter] to continue, press [CTRL+D] to quit.''')

input('>')

print('Let\'s go! ')
print('Please guess an integer betwenn 0 and 20(20 is included).')
print('You have 10 chance in total.')

a=random.randint(0,20)
n=0

while n<10:
	b=input('>')
	b=str(b)
	if b.isdigit():
		c=int(b)
		if c>a:
			print('Too big. Try it again! You have %d chance left.' %(9-n))
		elif c<a:
			print("Too small. Try it again!You have %d chance left." %(9-n))
		else:
			print("Congratulations! You got the right answer and used %d chance." %n)
			exit(0)
	else:
		print('Please enter an integer')

	n+=1

print("Sorry,time's up! Bad luck today:(")
