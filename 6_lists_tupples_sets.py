# Task 1. The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

from random import randint
new_list = [randint(0,100) for int in range(10)]
max_number = max(new_list)
print(f"Cписок: {new_list}. Максимальное число: {max_number}")
########################################
from random import randint
new_list = [randint(0,100) for int in range(10)]
i = 0
max_number = new_list[1]
while i < len(new_list):
    i +=1
    if new_list[1] > max_number:
        max_number = new_list[1]
    print(f"Cписок: {new_list}. Максимальное число: {max_number}")
    break

# Task 2. Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the
# common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

from random import randint
list_1 = [randint(0,10) for int in range(10)]
list_2 = [randint(0,10) for int in range(10)]
list_3 = list_1 + list_2
no_duplicates = list(set(list_3))
print('Cписок 1:', list_1, 'Cписок 2:', list_2, 'Общий список 1-2:', list_3, 'Cписок без дубликатов:',
      no_duplicates, sep='\n')

# Task 3. Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration
######################################
list_1 = list(range(1, 101))
list_2 = []
while True:
    if (list_1[76]) % 7 == 0 and (list_1[76]) % 5 != 0:
        list_2.append(list_1[76])
        print(list_2)
        break
######################################
list_1 = list(range(1, 101))
list_2 = []
index = 0
while index < len(list_1):
    index += 1
    while (len(list_1)+1) % 7 == 0 and (len(list_1)+1) % 5 != 0:
        list_2.append(len(list_1)+1)
#######################################
list_1 = []
list_2 = []
x = 0
while x <= 100:
    x += 1
    if x % 5 != 0 and x % 7 == 0:
        list_2.append(x)
        print(list_2)
#######################################

# Task 4. Реверс. Создайте лист длинной 10 с подряд идущими значениями. Используя цикл переверните лист.
# (для этого надо поменять первый с последним, второй с предпоследним и так далее)
from random import randint
list_1 = list(range(1, 11))
list_1.reverse()
print (list_1)
#######################################
list_1 = list(range(1, 11))

# Task 5.Преобразование типов и слайсы. Превратите полученную от пользователя строку в тапл.
# Выведите строку содержащую только буквы на четных позициях.


