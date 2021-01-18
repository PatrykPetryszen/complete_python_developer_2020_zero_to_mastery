import re

pattern = re.compile('this')
string = 'search this inside of this text please! Patryk'

# print('search' in string)
# a = re.search('this', string)
#print(a.span()) #This tells us where the string occurs

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(b)

#Lesson 189 for exercises
