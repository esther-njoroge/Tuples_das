friends = ("Claat", "Dylan", "Dorcas", "Kevin")
# accessing
print(friends)
print(type(friends))
print(len(friends))
print(friends[2])
print(friends[1:])

# Accessing using negative index
print(friends[-3])
print(friends[:-2])
print(friends[-4:])


fruits = ("mango", "kiwi", "melon" "apple", "banana")
print(tuple(fruits))

# concatination
newvar = (fruits + friends)

# Adding items
newOrder = list(fruits)
print(newOrder)
newOrder.extend(["berries", "oranges", "pineapples"])
print(newOrder)


# removing an item
print(newOrder.pop())

# printing each item 
for z in newOrder:
    print (z)

