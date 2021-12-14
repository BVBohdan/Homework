#Дополнительное задание доделаю, только сегодня забрал ноут с ремонта. Не успел еще к сожалению

# Task 1. A Person class.
# Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
# and add them as attributes. Make another method called talk() which makes prints a greeting from the person
# containing, for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old. '
              f'Ah sh*t, here we go again')

name = Person('Carl', 'Jhonson', '26')
name.talk()

# Task 2. Doggy age.
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which
# takes values for a dog’s age. Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self, ):
        return self.dog_age * self.age_factor

# Task 3. TV controller.
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
# exists in the list, or "No" - in the other case.

CHANNELS = ['BBC', 'Discovery', 'TV1000']

class TVController:
    def __init__(self, channels):
        self.channels = channels[0:]
        self.active_channel = self.channels.index(0)

    def first_channel(self):
        self.active_channel = self.channels.index(0)

    def last_channel(self):
        self.active_channel = self.channels.index(-1)

    def turn_channel(self, n):
        try:
            self.active_channel = self.channels.index(n-1)
        except IndexError:
            print('You chose wrong channel')

    # Второй вариант переключения канала
    # def turn_channel(self, n):
    #     if self.channel(n) <= len(self.channels):
    #         self.active_channel = n
    #     if self.channel(n) > len(self.channels):
    #         self.active_channel = n % self.channels

    def next_channel(self):
        if self.channels.index(self.active_channel) == len(self.active_channel) - 1:
            self.active_channel = self.channels.index(0)
        else:
            self.active_channel = self.channels[self.channels.index(self.active_channel) + 1]

    def previous_channel(self):
        if self.channels.index(self.active_channel) == 0:
            self.active_channel = self.channels.index(-1)
        else:
            self.active_channel = self.channels[self.channels.index(self.active_channel) - 1]

    def current_channel(self):
        return self.active_channel

    def is_exist(self, number):
        for n, name in enumerate(self.channels):
            if n == number + 1 or n == name:
                return 'YES'
            return 'NO'

controller = TVController(CHANNELS)
assert controller.first_channel() = "BBC"
assert controller.last_channel() = "TV1000"
assert controller.turn_channel(1) = "BBC"
assert controller.next_channel() = "Discovery"
assert controller.previous_channel() = "BBC"
assert controller.current_channel() = "BBC"
assert controller.is_exist(4) = "No"
assert controller.is_exist("BBC") = "Yes"

# Additional Task 1. Создайте класс Friend для хранения имени name и телефона phone.
# Обратите внимание, у друга может не быть телефона.
class Friend:
    def __init__(self, *information):
