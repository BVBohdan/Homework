# Task 1. Make a program that has some sentence (a string) on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.

sentence = 'table spoon tv bed spoon table chair receiver freezer chair table receiver'
sentence_2 = [w.strip() for w in sentence.split(' ')]
new_dict = dict((i, sentence_2.count(i)) for i in set(sentence_2))
print(new_dict)


# Task 2. Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.
# stock = {
# #     "banana": 6,
# #     "apple": 0,
# #     "orange": 32,
# #     "pear": 15
# # }
# # prices = {
# #     "banana": 4,
# #     "apple": 2,
# #     "orange": 1.5,
# #     "pear": 3
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
def dict_mul(stock, prices):
    c = dict()
    for k in stock:
        if k in prices:
            c[k] = stock[k] * prices[k]
    return c
print(dict_mul(stock, prices))


# Task 3. List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j`
# is corresponding to `i` squared.
list_1 = []
list_2 = []
list_3 = []
i = list(range(1, 11))
list_1.extend(i)
list_3.extend(list_1)
j = 0
while j < 11:
    j += i[0]
    list_2.append(j**2)
list_3.extend(list_2)
print(list_3)

list_1 = [(i, i**2) for i in range (1,11)]
print(list_1)