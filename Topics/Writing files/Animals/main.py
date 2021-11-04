# read animals.txt
# and write animals_new.txt
with open('animals.txt', 'r') as file_animals:
    animals = file_animals.readlines()
    amimals_with_spaces = [i.replace('\n', ' ') for i in animals]
with open('animals_new.txt', 'w') as new_animals:
    new_animals.writelines(amimals_with_spaces)
