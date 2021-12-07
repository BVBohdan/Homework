#
# Домашка ещё не закончена. Прошу повременить с выставлением оценки :)
#
# Task 1. Files
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents.
# Run your two scripts from the system command line.
# Does the new file show up in the directory where you ran your scripts?
# What if you add a different directory path to the filename passed to open?
# Note: file write methods do not add newline characters to your strings;
# add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.

import os
import shutil

my_file = open('myfile.txt', 'w+')
my_file.write('Hello file world!')
my_file.close()
my_file = open('myfile.txt')
my_file.read()
my_file = open('myfile.txt')
shutil.move('myfile.txt', 'new_myfile')




# Task 2. Extend Phonebook application
# Functionality of Phonebook application:
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
#
# The first argument to the application should be the name of the phonebook. Application should load JSON data,
# if it is present in the folder with application, else raise an error.
# After the user exits, all data should be saved to loaded JSON.


def creating_contact(phone, *wargs):
    new_contact = dict(phone='-', name='-', initials='-', city='-', country='-')
    new_contact['phone'] = input('Input phone number')
    new_contact['name'] = input('Input name')
    initial = new_contact.get('name')
    new_contact['initials'] = initial[0]
    new_contact['city'] = input('Input city')
    new_contact['country'] = input('Input country')
    return new_contact

def adding_contact():
    phonebook_file = open('Phonebook.json', 'w+')
    phonebook_file.write(creating_contact())
    phonebook_file.close()

def searching_contact():
    f = True
    name_id = input('Input name:')
    for i in new_contact:
        if new_contact.get('name').upper() == name_id.upper():
            print(new_contact.get('phone'), new_contact.get('name'), new_contact.get('initials'),
                  new_contact.get('city'), new_contact.get('country'))
            f = False
    if f:
        print('Name did not found')

def delete_contact():
    f = True
    name_id = input('Input name:')
    for i in new_contact:
        if new_contact.get('name').upper() == name_id.upper():
            new_contact.pop('name')
            f = False
    if f:
        print('Name did not found')