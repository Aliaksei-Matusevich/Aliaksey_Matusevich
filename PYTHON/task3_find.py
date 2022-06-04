string = input()
u_case = [letter for letter in string if 'A' <= letter <= 'Z']
print("Колличество заглавных букв:", len(u_case))
l_case = [letter for letter in string if 'a' <= letter <= 'z'] 
print("Колличество строчных букв:", len(l_case))
