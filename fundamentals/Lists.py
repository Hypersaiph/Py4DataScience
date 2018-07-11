list_1 = [5, 139, 478, 34, 10000, 24, 578, 4567]

print(type(list_1))

list_2 = ["yolo", 139, 478, False, not False, 24, 578, 4567.99]

print(type(list_2))

list_3 = ['is it ok?', not True, list]

print(type(list_3))

# multiple lists
y = list(range(8))
print(y)
# between
y = list(range(1, 8))
print(y)
# with steps
y = list(range(110, 201, 10))
print(y)

# access to lists
w = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(w[1])
print(w[2])
print(w[3])
print(len(w))
# negative indexation starts at the end of the list
print(w[-1])
print(w[-2])
print(w[-3])
w[-3] = ':3'
print(w)

# slicing
wii = ['A','B','C','D','E','F','G','H','I','j']
# everything
print(wii[:])
# starting from 2
print(wii[2:])
# until 7, 7 is not inclusive
print(wii[:7])
# range from 2 to 7, 7 is not inclusive
print(wii[2:7])
# range from 2 to 7, 7 is not inclusive
print(wii[-8:-3])

# [ADVANCED] slicing :D!!
# slice from 2 to element 9, 9th element is not inclusive
# getting every two members
print(wii[2:9:2])

# everything, step by 2
print(wii[::2])

