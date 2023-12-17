
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multuply(a, b):
    return a * b
def divide(a, b):
    return a / b
def sqr(a, b):
    return a ** b
def main():
    while True:
        print("Выберите операцию: ")
        print("1. Слодение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Выйти из программы")

        choice = input("Выберите операцию (1/2/3/4/5/6): ")

        if choice == '6':
            print("Выход из программы")
            break

        if choice not in ('1', '2', '3', '4', '5'):
            print("Неккоректный ввод, выберите число от 1 до 6")
            continue
        try:
            num1 = float(input("Введите первое число: "))
            if choice != '5':
                num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Введите число, а не сроку.")
            continue

        if  choice == '1':
            print(f"Результат: {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {multuply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Результат: {sqr(num1, num2)}")

if __name__ == "__main__":
    main()

