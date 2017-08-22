Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import rendom
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import rendom
ImportError: No module named 'rendom'
>>> import random
>>> a=range(10)
>>> random.shuffle(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    random.shuffle(a)
  File "/usr/lib/python3.5/random.py", line 272, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'range' object does not support item assignment
>>> print a
SyntaxError: Missing parentheses in call to 'print'
>>> prt a
SyntaxError: invalid syntax
>>> print(a)
range(0, 10)
>>> a=shuffleZ(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a=shuffleZ(a)
NameError: name 'shuffleZ' is not defined
>>> a=shuffle(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=shuffle(a)
NameError: name 'shuffle' is not defined
>>> a=random.shuffle(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a=random.shuffle(a)
  File "/usr/lib/python3.5/random.py", line 272, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'range' object does not support item assignment
>>> a.sort
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.sort
AttributeError: 'range' object has no attribute 'sort'
>>> print(a)
range(0, 10)
>>> dir random
SyntaxError: invalid syntax
>>> a=[1,2,3]
>>> print(a)
[1, 2, 3]
>>> a.sort
<built-in method sort of list object at 0x7feb45d43108>
>>> print(a)
[1, 2, 3]
>>> random.shuffle(a)
>>> print(a)
[2, 1, 3]
>>> a.sort
<built-in method sort of list object at 0x7feb45d43108>
>>> print(a)
[2, 1, 3]
>>> a.sort()
>>> print(a)
[1, 2, 3]
>>> 
