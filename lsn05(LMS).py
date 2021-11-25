#                                                       Lesson 5 LMS
# Task 1. The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random
a = random.randint (1,10)
b = int(input('Я загадал случайное число от 1 до 10 включительно. Поробуй угадать его'))
while True:
    if b == a:
        print ('Ты угадал')
        break
    elif b != a and 0 < b < 11:
        print ('Ты не угадал, я загадывал число', a)
        break
    b = int(input('Поробуй заново, число за рамками'))

# Task 2. The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

name = input('Введите Ваше имя')
age = int(input('Введите Ваш возраст'))
print('Привет,', name.capitalize(), 'в следующий день рождения тебе исполнится', age + 1, 'лет')

# Task 3. Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
# that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)

import random
word = input('Input your word')
word_length = 5
word_numbers = 5
while word_numbers > 0:
    word_numbers -= 1
    new_word = word
    the_word = ''
    while len(the_word) < word_length:
        index = random.randint(0,len(new_word)-1)
        the_word += new_word[index]
        new_word = new_word [0:index] + new_word[index+1:]
    print(the_word)

# Task 4. The math quiz program
# Write a program that asks the answer for a mathematical expression, checks whether
# the user is right or wrong, and then responds with a message accordingly.

a = int(input('Решите задачу: 25*x=75. Чему равно "x"?'))
x = 75/25
n = 0
while n < 5:
    n += 1
    if a == x:
        print('GG!WP!')
        break
    else:
        a = int(input('К сожалению решение не верно. Попробуй ещё раз. 25*x=75. Чему равно "x"?'))
print ('У тебя не получилось. Пользуйся калькулятором в магазинах')

# Task 5.Используя модуль random и его функции randint напишите игру "математика 5кл".
# y=2x+3 / y=3x+15 / y=x+7
import random
x = random.randint(0,30)
if 0 <= x <11:
    print('Реши уравнение y = 2x + 3, при x =', x)
    y = int(input('Чему равен "y"?'))
    while True:
        if y == 2*x + 3:
            print('Молодец, решение верно!')
            break
        else:
            print('Ты решил уравнение не верно, попробуй еще раз. Реши уравнение y = 2x + 3, при x =', x)
            y = int(input('Чему равен "y"?'))
elif 10 <= x <21:
    print('Реши уравнение y = 3x + 15, при x =', x)
    y = int(input('Чему равен "y"?'))
    while True:
        if y == 3 * x + 15:
            print('Молодец, решение верно!')
            break
        else:
            print('Ты решил уравнение не верно, попробуй еще раз. Реши уравнение y = 3x + 15, при x =', x)
            y = int(input('Чему равен "y"?'))
else:
    print('Реши уравнение y = x + 7, при x =', x)
    y = int(input('Чему равен "y"?'))
    while True:
        if y == x + 7:
            print('Молодец, решение верно!')
            break
        else:
            print('Ты решил уравнение не верно, попробуй еще раз. Реши уравнение y = x + 7, при x =', x)
            y = int(input('Чему равен "y"?'))