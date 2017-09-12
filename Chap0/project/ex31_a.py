print('Let\'s play a game named "Fortune teller" now!' )
print('Are you ready to go? Press “Return” to continue；Press "CTRL+D" to quit.')

input('>')

print('The first question is:Do you like cat or dog?')

animal = input('>')

if animal == "cat":
	print('Good! Then, do you like sunny day or rainy day? Well, if neither, which one do you prefer to have in your leisure time?')
	weather = input('>')
	if weather == "sunny day":
		print('Yeah! I can tell you are an outgoing person and you will have a surprise in two days.')
	else:
		print('Haha, Lord Cat bless you!')

elif animal == "dog":
	print('That\'s great! You will have a new friend in a week.')

else:
	print('Please check your spelling.')