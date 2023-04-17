a = [10,20,30,40,50]

a.append(5)
a.append(6)
a.append(7) # keeps order
print(a)

# 2 ways to remove elements
a.remove(50)
print(a)
a.pop(2) # removes element at index 2
print(a)
a.pop() # removes the last elements (treats it like a stack)
print(a)

a.sort()
print(a)

empty=[]
# for i in range(len(a))
for val in a:
    if val >= 6 or val <= 40:
        empty.append(val)

empty=[0] * 10 # creates an array with 10 0's
empty[5] = 10 # gives index place 5 a value
print(empty)

dog='dog'
three_dogs=dog*3
print(three_dogs)

# Comprehensions
squares = [i * i for i in range(1,10) if i%2==0]
print(squares)

# comprehension can iterate through an existing list
animals = ['dog', 'cat', 'dog', 'turtle']
dogs = [animal for animal in animals if animal=='dog'] # can put conditional animal=='dog'
print(dogs)

#Sets (can't have duplicates, unlike sets; unordered list of items)
a_set = {1,2,3,3,3,3}
print(a_set) # takes out additional 3s
a_list = [1,2,3,4,4,4,4]
no_dupes = set(a_list) # takes duplicates out of the list
print(no_dupes)

#Dictionaries
# key is a person and value is favorite food
fav_foods = {'Kathleen':'Pizza', 'Max':'Burgers', 'Matt':'Chicken Parm', 'Andy':'Ice Cream'}
mff=fav_foods['Matt']

for key in fav_foods:
    print(key, 'fav food is', fav_foods[key])

for key,val in fav_foods.items(): # can access key and value w this
    print(key, 'fav food is', val)

if 'Christina' in fav_foods:
    print(fav_foods['Christina'])
else:
    fav_foods['Christina']='Sushi'
print(fav_foods)
