from sys import getsizeof

print(getsizeof('Programando Ideias'))

print(getsizeof('10432432423423dvvvvvvv42342342432'))

#Utilizando list comprehension
print(getsizeof(num for num in range(1,1001)))

#Utilizando generators
print(getsizeof(num for num in range(1,1001)))