import re
pattern = "is"
pattern1 = r'[A-Z]+yclone'
text = "Grid Dynamics is very weel known organization Cyclone Dyclone Eyclone"
match = re.search(pattern, text)
print(match)
matches = re.finditer(pattern1, text)
for match1 in matches:
    print(match1)
    print(match1.span()) 
print(match)
print(match.span())
 