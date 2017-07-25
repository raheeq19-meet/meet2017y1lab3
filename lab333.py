Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> "don't" + "forget" + "to" + "converse" + "water"
"don'tforgettoconversewater"
>>> 'don't'
SyntaxError: invalid syntax
>>> 'Don't' + ' forget' +  'to' + ' conserve ' + 'water'
SyntaxError: invalid syntax
>>> "the"*3
'thethethe'
>>> 'the' + 3
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    'the' + 3
TypeError: Can't convert 'int' object to str implicitly
>>> "the"*3 + "beautiful" + "Earth"
'thethethebeautifulEarth'
>>> 2*"True"
'TrueTrue'
>>> 'TrueTrue'
'TrueTrue'
>>> a=save
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=save
NameError: name 'save' is not defined
>>> a='save'
>>> b='the'
>>> c='planet'
>>> print("a + b + c")
a + b + c
>>> print(a + b + c)
savetheplanet
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a="4 "
>>> b="panda bears"
>>> print(str(a) + b)
4 panda bears
>>> yay="Raheeq"
>>> yay.len()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    yay.len()
AttributeError: 'str' object has no attribute 'len'
>>> .len(yay)
SyntaxError: invalid syntax
>>> len(yay)
6
>>> upper(yay)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    upper(yay)
NameError: name 'upper' is not defined
>>> yay.upper()
'RAHEEQ'
>>> yay.lower()
'raheeq'
>>> yay.capitalize()
'Raheeq'
>>> yay.swapcase()
'rAHEEQ'
>>> yay.replace("r","l")
'Raheeq'
>>> bla= raheeq
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    bla= raheeq
NameError: name 'raheeq' is not defined
>>> bla= "raheeq"
>>> bla.capit
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    bla.capit
AttributeError: 'str' object has no attribute 'capit'
>>> bla.capitalize()
'Raheeq'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a= "MEET"
>>> b= "meet"
>>> c= "Meat"
>>> a==b
False
>>> a==c
False
>>> b==c
False
>>> a != b
True
>>> a!=c
True
>>> b!=c
True
>>> my_string = "bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: EOL while scanning string literal
>>> my_string="bananayellowthinkhatgreyBIGcalifornia314"
>>> my_string[12:18]
'thinkh'
>>> my_string[12:17 , 25:27]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    my_string[12:17 , 25:27]
TypeError: string indices must be integers
>>> my_string[12:17] + my_string[25:27]
'thinkIG'
>>> my_string[12:17 ] + my_string[24:27]
'thinkBIG'
>>> my_string[12:17 ] + my_string[ 24:27]
'thinkBIG'
>>> my_string[12:17 ] + my_string [ 24:27]
'thinkBIG'
>>> 
