import random

generated_letters = [x for x in range (97, 123)]

my_list = []

for letters in range(0, 101):
    index = random.randint(0, 25)
    letter = generated_letters[index]
    
    my_list.append(chr(letter))
    
print(my_list)

for letter in range(97, 123):
    print(chr(letter), my_list.count(chr(letter)), sep=": ")


# This piece of code generates 100 random characters then counts how many times a character is repeated
