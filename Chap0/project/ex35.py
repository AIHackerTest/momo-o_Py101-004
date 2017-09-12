from sys import exit

def bear_room():
	print('''
		Now you enter a room where a beer stands in fron of a room. 
		It has a bunch of honey in the room.
		What will you do?''')

	bear_moved=False

	while True:
		bear=input('>')

		if bear=="take honey":
			dead("The bear look at you then slaps your face off.")
		elif bear=="taunt bear" and not bear_moved:
			print('The bear has moved from the door. You can go through it now.')
			bear_moved=True
		elif bear=="taunt bear" and bear_moved:
			dead('The bear gets pissed off and chew your leg off.')
		elif bear=="open door" and bear_moved:
			gold_room()
		else:
			print('I got no idea what that means.')


def gold_room():
	print('This room is full of gold. How much do you take?')
	
	gold=input('>')

	if gold==int():
		how_much=int(gold)
	else:
		dead('Man, learn to type a number.')

	if how_much<50:
		print('Nice,you are not greedy, you win!')
		exit(0)
	else:
		dead('You greedy bastard!')

def cthulu_room():
	print('Here you see the great evil Cthulhu.')
	print('He, it, whatever stares at you and you go insane.')
	print('Do you flee for your life or eat your head?')

	next=input("flee/head?")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulu_room()

def dead(why):
	print(why,"Good job!")
	exit(0)

def start():
	print('''
		You are in a dark room.
		There is a door to your right and left.
		Which one do you take?''')
	next=input('>')

	if next=='left':
		bear_room()
	elif next=='right':
		cthulu_room()
	else:
		dead('You stumble around the room until you starve.')

start()




