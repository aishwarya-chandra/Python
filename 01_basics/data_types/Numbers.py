# #EXPRESSIONS
# x = 2
# y = 3
# z = 4
# print(x+y)     #add
# print(z-x)     #subtract
# print(x*y)     #product
# print(x/z)     #divide, gives answer in float form
# print(x ** y)  # x to the power y
# print(x // z)  #gives answer in integer form by truncating
# print(z % x)   #modulus, tells remiander

# #PRECEDENCE OPERATER
# print(x+y*z)             #bad production code
# print((x+y)*z)           #always use parenthesis

# #higher precison taken care
# print(40 + 2.23)         #gives float
# #good practice - use same data type
# print(float(40) + 2.23)

# #OPERATOR OVERLOADING
# print(1+2)
# print("aish"+"warya")

# #COMPARISONS
# print(1>2)
# print(1<2)
# print(1<=2)
# print(1>=2)
# print(2.0==2)
# print(2!=5)     #not equal to
# print(x<y<z)
# #OR
# print(x<y and y<z)
# print(1 == 2 < 3)
# #OR
# print(1 == 2 and 2 < 3)

# #LIBRARIES
# import math
# print(math.floor(3.5))
# print(math.floor(-3.5))
# print(math.trunc(2.8))             #trunc takes number towards zero
# print(math.trunc(-2.8))

# #COMPLEX NUMBERS
# print((2 + 1j)*3)

# #OCTAL BASE 8
# print(0o20)
# print(oct(64))

# #HEX BASE 16
# print(0xFF)
# print(hex(64))

# #BINARY BASE 2
# print(0b1000)
# print(bin(64))

# #Using int() to convert any base to decimal
# print(int('64', 8))                
# print(int('64', 16))
# print(int('10000', 2))     

# #BITWISE OPERATIONS
# print(x << 2)  #left-shift (Shifts bits to the left)
# print(x | 2)   #or
# print(5 & 3)   #and
# print(5 ^ 3)   #xor
# print(~5)      #not (Inverts all the bits (1’s complement))
# print(5 >> 1)  #right-shift (Shifts bits to the right)

# #RANDOM
# import random
# print(random.random())
# print(random.randint(1,10))  #10 not included
# print(random.choice([1,4,6,8,9]))
# list = ['cat', 'dog', 'otter', 'owl', 'capybara']
# print(random.choice(list))
# print(random.shuffle(list))           #Shuffle list in place, and return None.
# print(list)

# #DECIMAL
# print((0.1 + 0.1 + 0.1) - 0.3)          #Floating-point numbers like 0.1 and 0.3 can’t be exactly represented in binary, it results in a very tiny rounding error, not exactly 0.
# from decimal import Decimal               #read about decimal context manager
# print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

# #FRACTIONS
# from fractions import Fraction
# print(Fraction(2,7))

#BOOLEAN
print(True == 1)
print(True + 4)