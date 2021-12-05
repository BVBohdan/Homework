# Addition Task 1. Напишите функцию которая будет переводить возраст с Земного на Марсианский.
# В году на Земле 365 дней а на марсе 687

def mars_age(earth_age):
    mars_age = (earth_age * 365) // 687
    return mars_age

assert mars_age(10) == 5
assert mars_age(63) == 33
assert mars_age(1000) == 531

# Addition Task 2.Напишите функцию greet принимающую имя name (type:str) м слово word (type:str).
# Если слово не передано то считать его " -" и возвращающую строку вида "[Имя] ты сегодня [слово]!"

def greet (name, word = '-'):
    return f'{str(name)}, ты сегодня {str(word)}!'

assert greet("111", "2") == "111 ты сегодня 2!"
assert greet("игорь", "молодец") == "Игорь ты сегодня молодец!"
assert greet(name="ольга", word="супер") == "Ольга ты сегодня супер!"
assert greet("николай") == "Николай ты сегодня -!"

# Addition Task 3. Напишите функцию joinA которая принимает неограниченное количество значений любого типа и
# возвращает строку где эти значения склеены через символ A

def joinA(*args):
    a = 'A'.join(str(n) for n in args)
    return a

assert joinA("Привет", "мир", "!") == "ПриветAмирA!"
assert joinA("Привет", 1, 2, 3, True) == "ПриветA1A2A3ATrue"
assert joinA() == ""

# Task 1. Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def opps():
    raise IndexError

def error_catcher():
    try:
        opps()
    except IndexError:
        print('IndexError')
    except:
        print('KeyError')

# Task 2. Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b, construct a try-except block
# which raises an exception if the two values given by the input function were not numbers, and if value b was zero
# (cannot divide by zero).

a = int(input())
b = int(input())
def two_numbers(a,b):
    try:
        c = a**2 / b
        return c
    except ValueError:
        print('values given by the input are not numbers')
    except Devive_by_Zero_Error:
        print("You can't divide by zero")
rez = two_numbers(a,b)
if rez != None:
    print(rez)


