def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: division by zero"

def subtraction(a, b):
    return a - b

def quadratic_equation(a, b, c):
    # Рассчитываем дискриминант
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + (discriminant ** 0.5)) / (2*a)
        root2 = (-b - (discriminant ** 0.5)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return "Уравнение не имеет действительных корней"

# Получение входных данных от пользователя
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

# Пример использования функций с введенными значениями
print("Сложение:", addition(a, b))
print("Умножение:", multiplication(a, b))
print("Деление:", division(a, b))
print("Вычитание:", subtraction(a, b))

результат_уравнения = quadratic_equation(a, b, c)
if isinstance(результат_уравнения, tuple):
    print("Корни квадратного уравнения:", результат_уравнения)
else:
    print(результат_уравнения)
