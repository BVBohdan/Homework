#Задание 1. Допишите код так, чтобы меняя значение переменной day_of_week выводились следующие сообщения
# 'рабочий деньʼ, 'выходной', 'Ошибка! Дни недели считаются 1-7 ни больше ни меньше!'
a = int (input())
if 1<=a<=5:
    print ('рабочий день')
elif 5<a<8:
    print ('выходной')
else:
    print ('ошибка')


# Задание 2. У вас есть переменные holiday, day_of_week, wallet проставьте условия в код.
# попробуйте менять исходные значения чтоб убедиться что все
holiday, day_of_week, wallet = False, 6, 50000
if ((not holiday) or day_of_week) and wallet<5000:
    print("оно то и можно погулять но не на что")
elif ((not holiday) or day_of_week) and wallet<=5000:
    print("пиво и чипсы на большее денег нет")
elif ( holiday or (not day_of_week)) and wallet>5000:
    print("гуляем в ресторане, всех угощаю")
elif wallet>5000:
    print("После Безоса следующим лечу я. И моя любимая кошка!")
else:
    print("работаем")


# Задание 3. Выведите значения у для х в пределах от 0 до 100 c шагом 1 если y = 3x + 12
x = 0
while 0 <= x < 101:
    x += 1
    y = 3 * x + 12
    print(y)


# Задание 4. Провалидируйте введенный пользователем номер телефона.
# - начинается с +3
# - код оператора один из 050 067 099 063
# - длинна правильная попробуйте менять значение номера чтоб убедиться что ваши условия
# - отрабатывают правильно.
#phone = '+380987362338' +321123456123
# ваш код
phone = '+380987362338'
contry_code = phone[0:3]
number_code = phone[3:6]
if len(phone) == 13 and contry_code == ('+38') and (
        number_code == '050' or number_code == '098' or number_code == '093'):
    print("Correct Number")
else:
    print("Your number isn't correct")

# Задание 5. Используя функцию input получаем от пользователя строку.
# Напишите код в котором просим дать ответ на загадку.
# Если человек сдается он вводит q или Q и прерываем цикл while.
# Если угадал - выводим поздравление. Если нет - пристыдите его.
# Ответ принимается регистронезависимо.

print('Отгадай загадку. Маленькое беленькое на потолке висит не светит')
answer = input()
if answer == 'q':
    print('Слабак')
elif answer == 'Лампочка' or 'лампочка' or 'ЛАМПОЧКА':
    print('Поздравляю! Ты решил эту загадку')
else:
    print('Шейм он ю. Ответ знает даже ребенок. Пробуй ещё раз, не буди во мне внутреннего зверя, харёк пока спит спокойно')
    answer +=1


answer = input('Отгадай загадку. Маленькое беленькое на потолке висит не светит')
while True:
    if answer.lower() == 'q':
        print('пока')
        break
    if answer.lower() == 'лампочка':
        print('Поздравляю! Ты решил эту загадку')
        break

    print('Шейм он ю. Ответ знает даже ребенок. Пробуй ещё раз, не буди во мне внутреннего зверя, харёк пока спит спокойно')
    answer = input('Отгадай загадку. Маленькое беленькое на потолке висит не светит')




# Задание 6. Наверняка вам доводилось связываться с оператором мобильной связи.
# С помощью вложенных if и чувства меры опишите систему где ответ человека принимается через input
# и дальшейшее общение продолжается в новом "ключе" Сделайте возможным из любого места нажать q и
# прервать мучения пользователя.
# Например:
x = int(input('Здравствуй, если хочешь узнать акции нажми 1, если тариф 2, если погоду 3'))
if x == 1:
    print('К сожалению, сейчас нет достуных акций.')
if x == 2:
    x = int(input('Узнать свой тариф нажми 1, новые тарифы, нажми - 2, остаток по счету - 3'))
    if x == 1:
        print('Твой тариф - мега луп')
    elif x == 2:
        print('Новые тарифы не доступны')
    elif x == 3:
        print('Узнать остаток по основному счету - 1, остаток по бонусному 2')
        x = int(input())
        if x == 1:
            print('Остаток в гривнах - 1, гигабайтах - 2')
            x=int(input())
            if x == 1:
                print ('осталось 5 гривен')
            elif x == 2:
                print ('осталось 17 гигабайт')
        elif x == 2:
            print('На Вашем бонусном счету 3 гривны, 50 копеек')
if x == 3:
    print('Метео станция попала под бурю и не работает. Скорее всего вам тоже не повезет в скорем времени')


-> здравствуй, если хочешь узнать акции нажми 1, если тариф 2, если погоду 3
<- 2
->  узнать свой тариф 1, новые тарифы 2, остаток по счету 3
<- 3
->  остаток по основному счету 1 остаток по бонусному 2
<- 1
->  остаток в гривнах 1 остаток в минутах/гигабайтах 2
<- 1
->  на вашем счету 5 грн
(стрелочки это направление вывод или ввод данных. В консоли они не выводятся)

# Задание 7. Упрощение уравнения с картинки
# задача (1:1/2:2/5:5/5:10) 30.375 / 972.0 / 94921.875 / 1220703.125
x = int(input())
a = int(input())
y = ((2 + x/a)**3)*((x**2 + 4*(a**2) + 4*a*x)/8*(a**3))
print (y)
# 1 ответ (1:1/2:2/5:5/5:10) 24 / 48 / 120 / 200
x = int(input())
a = int(input())
y = 8*(2*a + x)
print (y)
# 2 ответ (1:1/2:2/5:5/5:10) 2.6666666666666665 / 1.3333333333333333 / 0.5333333333333333 / 0.32
x = int(input())
a = int(input())
y = 8/(x + 2*a)
print (y)
# 3 ответ (1:1/2:2/5:5/5:10) 0.375 / 0.75 / 1.875 / 3.125
x = int(input())
a = int(input())
y = (x + 2*a)/8
print (y)
# 4 ответ (1:1/2:2/5:5/5:10) 0.041666666666666664 / 0.020833333333333332 / 0.008333333333333333 / 0.005
x = int(input())
a = int(input())
y = 1/(8*(x + 2*a))
print (y)

                                                #LMS (Lesson4)
# Task 1 String manipulation
#Write a Python program to get a string made of the first 2 and the last 2 chars from
#a given string. If the string length is less than 2, return instead of the empty string.
#Sample String: 'helloworld'
#Expected Result : 'held'
#Sample String: 'my'
#Expected Result : 'mymy'
#Sample String: ' x'
#Expected Result: Empty String

a = input()
x = a[0:2] + a[-1:-2]
y = a*2
z = a*0
if 2 <= len(a):
    print (a, x, y, z, sep='\n')
else:
    print()

# Task 3
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”, it should return True.

name = 'mahamudkenitumash'
asked_name = input()
if name == asked_name.lower():
    print (True)
else:
    print (False)