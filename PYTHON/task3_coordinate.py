#Уравнение прямой вида y = kx + b задано в виде строки. Определить координату y точки с заданной координатой x. k и b всегда в наличии, 
# всегда неотрицательны.
#Примеры: Для строки y=5x+6 ответ k=5 и b=6; Для строки y=10+0x ответ k=0 и b=10; Для строки 0 + 1x = y ответ k=1 и b=0
string = "y=3.5x+76"
kb = string.replace("+", "=").replace("x", "").split("=")
if float(kb[1]) or int(kb[1]):
    print("k =", kb[1])
if float(kb[2]) or int(kb[2]):
    print("b =", kb[2])
