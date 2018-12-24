#2.1 Разработать прототип программы «Калькулятор», позволяющую выполнять базовые арифметические действия и функцию обертку, 
#сохраняющую название выполняемой операции, аргументы и результат в файл
#2.2 Дополнение программы «Калькулятор» декоратором, сохраняющий действия, которые выполняются в файл-журнал.
#2.3 Рефакторинг (модификация) программы с декоратором модулем functools
#2.4 Формирование отчета по практическому заданию и публикация его в портфолио.
#Вариативное задание

#2.3 Разработка функции-декоратора, вычисляющей время выполнения декорируемой функции.

def logger(function):
    import functools
    import datetime
    @functools.wraps(function)
    def wrapper(*args):
       
        if function.__name__ == 'summ':
            operation_name = "Сложение"
        elif function.__name__ == 'razn':
            operation_name = "Вычитание"
        elif function.__name__ == 'umn':
            operation_name = "Умножение"
        elif function.__name__ == 'dell':
            operation_name = "Деление"
        else:
            operation_name = "Неизвестная операция"
        
        time = datetime.datetime.now()
        result = function(*args)
        time = datetime.datetime.now() - time
        

        with open('Record.txt', 'a') as f:
            f.write("\n")
            f.write("Функция: " + operation_name + "\n")
            f.write("Аргументы: " + str(args) + "\n")
            f.write("Результат: " + str(result) + "\n")
            f.write("Время выполнения декорируемой функции " +  str(time))
            f.write("\n")
            f.write("\n")
        return result
        
    return wrapper


@logger
def summ(*args):
    res = 0
    for arg in args:
        res += arg
    return res

@logger
def razn(*args):
    args = list(args)
    res = args.pop(0)
    for arg in args:
        res -= arg
    return res

@logger
def umn(*args):
    res = 1
    for arg in args:
        res *= arg
    return res

@logger
def dell(*args):
    args = list(args)
    res = args.pop(0)
    for arg in args:
        res /= arg
    return res


@logger
def calc():

    choice = input(' Введите номер действия: \n (1.Сложение, 2.Вычитание, 3.Умножение, 4.Деление)\n')

    if choice == '1':
        print('Введите слагаемые через пробел:')
        arr = input().split()
        arr = list(map(int, arr))
        result = summ(*arr)
        print("Ответ:", result)
    elif choice == '2':
        print('Введите уменьшаемое и вычитаемые через пробел:')
        arr = input().split()
        arr = list(map(int, arr))
        result = razn(*arr)
        print("Ответ:", result)
    elif choice == '3':
        print('Введите множители через пробел: ')
        arr = input().split()
        arr = list(map(int, arr))
        result = umn(*arr)
        print("Ответ:", result)
    elif choice == '4':
        print('Делимое и делители:')
        arr = input().split()
        arr = list(map(int, arr))
        result = dell(*arr)
        print("Результат:", result)
    else:
        print('Некорректный ввод')
calc()
