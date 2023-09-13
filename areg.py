def add(x, y):
    return (x+y)
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Вас приветствует Арег")
print("Выберите операцию:")
print("m. Сложение")
print("z. Вычитание")
print("d. Умножение")
print("k. Деление")
choice = input("Введите номер операции (1-4): ")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if choice == 'm':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == 'z':
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == 'd':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == 'k':
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print("Повторите попытку")