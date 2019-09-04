from random import randint
import time
import os


numbers = []
guess = []

for i in range(1,9):
	numbers.append(randint(100000, 999999)) #generate 8 six digit numbers

for numbre in numbers:
	print(numbre)
	time.sleep(10) #waits 10 second
	os.system('cls') #clear screen
	guess.append(int(input('inter the number: '))) #get user guess
	os.system('cls') #clear screen
	
print('real   guess  result')
number_of_trues=0

for i in range(0,8):
	if numbers[i]==guess[i]:
		result=True
		number_of_trues += 1
	else:
		result=False
	print(numbers[i],guess[i],result)

print(number_of_trues,'True from 8')