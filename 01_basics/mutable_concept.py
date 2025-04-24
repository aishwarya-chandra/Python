l1 = [1,2,3]
l2 = l1         #referncing to same object created
print(l1)
print(l2)
l1[0] = 40      #as list is mutable, the 0th index of the object is changed
print(l1) 
print(l2)       #still references to l1

print("Another")    #ANOTHER EXAMPLE
p1 = [1,2,3]
p2 = p1         #referncing to same object created
p2 = [1,2,3]    #new object created and referenced to p2
print(p1)
print(p2)
p1[0] = 100     #this change will show only in p1, because p2 do not refernce p1 now.
print(p1)  
print(p2)

print("Another")    #ANOTHER EXAMPLE
h1 = [1,2,3]
h2 = h1[:]          #this is slicing, when sliced a copy is generated, hence references are not pointing to same object.
print(h1)
print(h2)
h1[0] = 50
print(h1)
print(h2)

print("How to check if referncing same object in the memory")
n = [1,2,3]
m = n
print(m==n)         #tells if both are equivalent
print(m is n)       #tells if referncing same object in the memory
m = [1,2,3]
print(m==n)
print(m is n)