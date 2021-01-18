#At least 8 char long
# contain any sort letters, numbers $%#@

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string= 'Patryk@gmail.com'
pattern2= re.compile(r"[A-Z-a-z0-9$%#@]{8,}\d")
password= 'kjhkjghffgj%$8'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)           