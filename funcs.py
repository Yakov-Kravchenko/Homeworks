def easy_func():
    a = int(input('Введите число:'))
    b = 5
    n = a + b
    if n == 10:
       print('Всё правильно!')
    else:
       print('Неверно')

def medium_func():
   num = int(input('Введите число:'))
   num2 = num + 2
   while True:
      if num2 == 8:
        print('Всё нормально')
        break
      else:
        print('Попробуйте ещё раз')
medium_func()
