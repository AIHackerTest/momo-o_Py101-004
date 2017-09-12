def list_loop(x,y):
	"Print a list of numbers from 0 with a step of y,and the last number in the list is less than x."
	i=0
	numbers=[]

	while i<x:
		print('Top is %d' %i)
		numbers.append(i)

		i+=y
		print('Numbers now:',numbers)

	print('The numbers:')
	for num in numbers:
		print(num)


print('The numbers:')
for num in range(0,19,3):
	print(num)