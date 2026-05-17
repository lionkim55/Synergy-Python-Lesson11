#[720, 120, 24, 6, 2, 1]

def factorial(number):
    result = 1
    
    for i in range(1, number + 1):
        result = result * i

    return result

n = int(input("Введите натуральное целое число: "))

if n < 1:
    print("Ошибка: нужно ввести натуральное число, то есть число от 1 и больше.")
else:
    main_factorial = factorial(n)

    print("Факториал введённого числа:", main_factorial)

    factorials_list = []

    for i in range(main_factorial, 0, -1):
        factorials_list.append(factorial(i))

    print("Список факториалов:", factorials_list)