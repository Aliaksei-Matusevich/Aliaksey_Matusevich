side_a = int(input())
side_b = int(input())
side_c = int(input())
semi_perimetr = (side_a + side_b + side_c) / 2
if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
    import math
    S = math.sqrt(semi_perimetr * (semi_perimetr - side_a) * (semi_perimetr - side_b) * (semi_perimetr - side_c))
    if side_a == side_b == side_c:
        print("Равносторонний.", "Площадь такого треугольника равна", S)
    elif side_c == side_b != side_a or side_b != side_c == side_a or side_b == side_a != side_c:
        print("Равнобедренный.", "Площадь такого треугольника равна", S)
    elif side_b**2 == side_a**2 + side_c**2 or side_a**2 == side_b**2 + side_c**2 or side_c**2 == side_b**2 + side_a**2:
        print("Прямоугольный.", "Площадь такого треугольника равна", S)
    else:
        print("Разносторонний.", "Площадь такого треугольника равна", S)
else:
    print("Wrong input data")