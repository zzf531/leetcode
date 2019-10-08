import random
'''
1、X等于mid，退出程序。
2、X大于mid，将start改为mid+1，继续递归，直至mid等于X。
3、X小于mid，将end改为mid-1，继续递归，直至mid等于X。
'''

import random

result = random.randrange(100)
lower = 0
upper = 100

while 1:
    input_number = input('Enter your number(%s - %s): '%(lower, upper))
    if input_number.isdigit():
        number = int(input_number)
        if number == result:
            print ('Congratulations, the number is %s.'%result)
            break
        elif upper > number > result:
            upper = number
        elif lower < number < result:
            lower = number
    else:
        print ('Please enter a number between 0 - 100')



