"""
Задание 4 Калькулятор

Создать скрипт, который просит ввести ввести число, операцию и снова число и выводит на экран ответ.
Скрипт должен поддерживать стандартные арифметические операции операции: +, -, /, *,
на остальные операции выдать сообщение об ошибке. Обратите внимание, что на 0 делить нельзя,
потому продумайте эту ситуацию.

Примечание! Пользоваться циклами запрещено.

Пример:
-Введите первое число:
>> 1
-Введите операцию:
>>+
-Введите второе число:
>> 2
- Ответ: 3


Пример 2:
-Введите первое число:
>> 1
-Введите операцию:
>>/
-Введите второе число:
>> 0
- Ошибка! На 0 делить нельзя

"""
numbOne = input('введите первое число ')
numbOne = int(numbOne)

Op = input('введите операцию: 1.сложение; 2.вычитание; 3.умножение; 4.деление ')
Op = int(Op)
numbTwo = input('введите второе число ')
numbTwo = int(numbTwo)



if Op == 1:
    print(numbOne + numbTwo)

elif Op == 2:
    print(numbOne - numbTwo)

elif Op == 3:
    print(numbOne * numbTwo)

elif Op == 4:
    if numbTwo == 0:
        print('на ноль делить нелзя')
    else:
        print(numbOne / numbTwo)

else:
    print('такой операции нет')
    