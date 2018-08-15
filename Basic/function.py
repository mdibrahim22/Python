#use of function
def myfunction(name):
	print('my name is: ', name)
def myfunction2(num1,num2):
	result = num1 + num2
	print('Sum is: ', result)

x = input('Please enter your name :')
num1 = int(input('Please enter your first number :'))
num2 = int(input('Please enter your second number :'))
myfunction(x)
myfunction2(num1,num2)