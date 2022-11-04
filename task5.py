from random import sample
def countdown():
    a = (sample(range(0,10), 10))
    print("Ваш список рандомных чисел: ", a)
    a.sort()
    a.reverse()
    for b in a:
         print(b, end=' ')
         if b != 0:
             continue
         print('Пуск!', end=' ')


countdown()