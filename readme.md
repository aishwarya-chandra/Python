# INNER WORKING OF PYTHON
![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

# COMPILER OF PYTHON
C, C++

# MUTABLE AND IMMUTABLE
![alt text](image-4.png)

# IMMUTABLE MEANING
Python assigns a memory and creates reference to that memory where everything is stored as an object assigned particular memory references. Changing reference (for eg: animal = "cat" , animal = "dog" [animal pointed to cat reference and then to dog reference , note that "dog" was not overwritten at assigned memory of "cat" {which happens in data types which are mutable}]) is allowed but changing value inside the assigned memory created ("cat" or "dog") is not allowed i.e, are immutable. If an assigned memory is not being referenced by anyone, garbage collector deletes it from the memory.
## example: a = a+2
given a = 5 and b = 2
![alt text](image-3.png)