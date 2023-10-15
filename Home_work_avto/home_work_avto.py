'''
Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.
Приклад файлу:
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.
Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і повертати загальну суму заробітної плати всіх розробників компанії.
Вимоги до завдання:
функція total_salary повертає значення типу float
для читання файлу функція total_salary використовує лише метод readline
ми поки що не використовуємо менеджер контексту with
'''

# def total_salary(path):
#     file = open(path, 'r')
#     res = 0.0
    
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         split_line = line.strip().split(',')
#         res = res + float(split_line[1])
       
#     file.close()
#     return res
 
# print(total_salary('d:\IT\GoIT\Modul_6\Home_work_avto\salery.txt'))

'''
У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:
['Robert Stivenson,28', 'Alex Denver,30']
Це список рядків із прізвищем та віком співробітника, розділеними комами.
Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з нового рядка.
Функція запису в файл write_employees_to_file(employee_list, path), де:
path – шлях до файлу.
employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
[['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
Вимоги:
запишіть вміст employee_list у файл, використовуючи режим "w".
ми поки що не використовуємо менеджер контексту with
кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:
Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
'''
# def write_employees_to_file(employee_list, path):
#     fh = open(path, 'w')
#     for item in employee_list:
#         for i in item:
#             fh.write(str(i) + '\n')
#     fh.close()
#     return fh

# print(write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'd:\IT\GoIT\Modul_6\Home_work_avto\worker_list.txt'))

'''
У попередній задачі ми записали співробітників у файл у такому вигляді:
Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу та повертатиме список співробітників у вигляді:
['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати при додаванні прочитаного рядка до списку.
Вимоги:
прочитайте вміст файлу за допомогою режиму "r".
ми поки що не використовуємо менеджер контексту with
поверніть із функції список співробітників із файлу
'''
def read_employees_from_file(path):
    fh = open(path, 'r')
    line = []
    while True:
        for i in fh.readlines():
            i = str(i).replace('\n', '')
            line.append(i)
            continue
        fh.close()
        return line

print(read_employees_from_file('d:\IT\GoIT\Modul_6\Home_work_avto\worker_list.txt'))

'''
Реалізуйте функцію add_employee_to_file(record, path), яка у файл (параметр path - шлях до файлу) буде додавати співробітника (параметр record) у вигляді рядка "Drake Mikelsson,19".
Вимоги:
параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
кожен запис у файл має починатися з нового рядка.
необхідно щоб стара інформація у файлі теж зберігалася, тому при роботі з файлом відкрийте файл у режимі 'a', додайте співробітника record у файл і закрийте його
ми поки що не використовуємо менеджер контексту with
'''