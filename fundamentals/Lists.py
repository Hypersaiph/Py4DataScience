
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
y = list(range(1,8))
print(y)
# with steps
y = list(range(110,201,10))
print(y)


# access to lists
w = ['a','b','c','d','e','f','g']
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