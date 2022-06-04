#задание работает некорректно
import re
string = input()  
u_case = [letter for letter in string if re.findall(r'^[a-zA-Z]+$', string) if letter.isupper()]
print("Колличество заглавных букв:", len(u_case))
l_case = [letter for letter in string if re.search(r'^[a-zA-Z]+$', string) if letter.islower()] 
print("Колличество строчных букв:", len(l_case))