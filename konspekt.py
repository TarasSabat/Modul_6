"""
Читання та запис у файл.
"""
# file = open('text.txt')  # якщо відкриваємий файл знаходиться в одній папці з файлом-програмою - вказувати шлях не потрібно  
#                          # якщо файла немає то буде вийняток
# print(file)              # показує атрибути файла
# print(file.name)         # атрибут name показує імя файла
# print(file.mode)         # атрибут mode показує режим в якому відкритий файл (по умовчаню r read (читання))
# print(file.closed)       # атрибут closed показує чи відкритий файл на даний час  

# file = file.read()       # повністю зчитує вміст файла (в дужках можна вказати кількість байт для считування)
# print(file)

# file.close()             # файл потрібно завжди закривати !!!      
# file.closed 

'''
Алгоритм зчитування файлу частинами (chang)
'''
# file = open('text.txt', 'r') # по замовчуванню файл відкривається для читання 'r'

# while True:
#     text = file.read (5)
#     print(text)
#     if not text:
#         break

# file.close()

'''
Способи читання файлу
'''
# file = open('text.txt', 'r')
# print(file.readline())            # зчитує один рядок
# print(file.readlines())           # зчитує усі строки відразу і повертає список, елементами якого є рядки та \n(ентер)
# file.close()

'''
Ітерування файлу
'''
# file = open('text.txt', 'r')        # при ітерації текст файла виводиться рядками 

# for line in file:
#     print(line)

# file.close()

'''
Запис у файл
'''
# file = open('text.txt', 'a')
# file.write('\nHello Ukraine\n')                           # добавляння тексту
# file. writelines(['First lines\n', 'Sekond lines\n'])     # добавляння списку рядків

# file.close()

'''
Запис у файл у визначене місце (5)
'''
# with open('text.txt', 'r+') as file:       # 'r+' - режим читання і записування на початок тексту
#     file.seek(5)
#     file.write('\nHello Ukraine\n')
# file.close()

'''
Рух курсору по тексту
'''
# file = open('text.txt', 'r')
# file.read(1)            # зчитує вказану кількіст байт
# print(file.tell())      # виводить інформацію де знаходиться курсор
# file.seek (6)           # поміщає курсор на вказану позицію (кількість байт) 
# file.close()

'''
Переіменування назви файлу
'''
# import os

# os.rename('asd.txt', 'text.txt')

'''
Переміщення файлу
'''
# import os

# os.rename('text.txt', r'Home_wotk\text.txt') - якщо такий файл вже є то rename не спрацює

## або

# os.replace('text.txt', r'Home_wotk\asd.txt') - якщо такий файл вже є то replace його замінить

'''
Рекурсивний рух по папках (не дороблено)
'''
# import os

# print(os.getcwd())

# def walk(path, prev_list_dir):

#     print(os.getcwd())

#     os.chdir(path)

#     list_dir = list(filter(os.path.isdir, os.listdir()))

#     for el in list_dir:
#         list_dir.remove(el)
#         walk(fr'{path}\{el}', list_dir)

# print(walk(r'D:\IT\GoIT\Modul_6\Home_work', []))


'''
Обхід вийнятків з метою закриття файлу
'''
# file = open('text.txt', 'a')
# file.write('Hello Taras\n')

# try:
#     raise TypeError
# except TypeError:
#     pass
# finally:
#     file.close()

#------------- або за допомогою with

# with open('text.txt', 'a') as file:   # при виході за межі контекста (4 пробіли) файл закриється автоматично
#     file.write('Hello Taras\n')
#     raise ValueError
# print(file.closed)

'''
Байт рядок
'''
# with open('text.txt', 'ab') as file:    # відкриття в змішаному режимі додавання байтами
#     file.write(b'Taras')                # при зчитуванні в режимі 'r' отримаємо рядок, в режимі 'rb' отримаємо байти 
# file.close()

# 'Taras'.encode()  - пертворює строку в байт рядок
'''
Кодування
'''
# b_array = bytearray(b'asdzxc')    # масив байт
# print(b_array)

# bytearray(b'asdzxc')              # переведення масив байта в строку (отримаєм порядковий новер згідно ASCII)
# print(list(b_array))              # з bytearray можна працювати як зі списком (по індексах)

# ----- Код Цезара (кодування і розкодовування)-------

# def encrypt(b_obj,key):              # перетворення в байт-масив   
#     b_obj_array = bytearray(b_obj)
#     for i, b in enumerate(b_obj_array):
#         n = b + key
#         if n > 255:
#             n -= 255
#         b_obj_array[i] = n
#     return bytes(b_obj_array) 

# def dekrypt(b_obj,key):              # функція декрипту
#     b_obj_array = bytearray(b_obj)        
#     for i, b in enumerate(b_obj_array):
#         n = b - key
#         if n < 0:
#             n += 255
#         b_obj_array[i] = n
#     return bytes(b_obj_array) 

# if __name__ == '__main__':
    
#     pwd = input('Enter your password: ')       # запис в файл
#     pwd_bytrs = pwd.encode()
#     encrypted_pwd = encrypt(pwd_bytrs, 200)

#     with open ('password.txt', 'wb') as file:
#         file.write(encrypted_pwd) 

#     with open ('password.txt', 'rb') as file:
#         encrypted_pwd = file.read()
#         print(encrypted_pwd)

#     print(dekrypt(encrypted_pwd, 200))

'''
--------------
'''

# file = open('test.txt', 'w', encoding='utf-8')
# file.write('Hello Test\n')
# file.write('Hello Ukraine\n')
# file.writelines(['Hi Vova\n', 'Hi Olga\n', 'Hi Iryna\n'])
# file.close()

# file = open('test.txt', 'r', encoding='utf-8')
# # result = file.read()
# # result = file.readline()            # зчитує один рядок
# result = file.readlines()             # зчитує усі строки відразу і повертає список, елементами якого є рядки
# print(result)
# file.close()

"""
Добавити запис в існуючий файл
"""
# file = open('test.txt', 'r', encoding='utf-8')
# file.write('Happy!!!')
# file.close()

"""
Прочитати перші N рядків файлу.
Ім'я файлу для читання передаємо як аргумент командного рядка
"""
# import sys
# NUMBER_LINES = 4

# if len(sys.argv) != 2:
#     print('Потрібно передати імя файлу для читання!')
#     quit()

# try:
#     file = open(sys.argv[1], 'r', encoding='utf-8')
#     line = file.readline()
#     count = 0
#     while count < NUMBER_LINES and line != '':
#         line = line.strip()
#         count += 1
#         print(line)
#         line = file.readline()
#     file.close()
# except OSError as error:
#     print(f'Error is: {error}')

"""
Прочитати хвіст файлу останні N рядків файлу.
Ім'я файлу для читання передаємо як аргумент командного рядка
"""
# import sys
# NUMBER_LINES = 4

# if len(sys.argv) != 2:
#     print('Потрібно передати імя файлу для читання!')
#     quit()

# try:
#     lines = []
#     with open(sys.argv[1], 'r', encoding='utf-8') as file:
#         for line in file:  # те саме що і file.readline()
#             lines.append(line)
#             if len(lines) > NUMBER_LINES:
#                 lines.pop(0)
#     print(lines)
# except OSError as error:
#     print(f'Error is: {error}')

"""
Читаємо файл за допомогою бібліотеки pathlib
"""
# from pathlib import Path

# folder = Path('./Temp')

# file_name = folder / 'temp.txt'

# print(file_name)
# try:
#     with open(file_name, 'r', encoding='utf-8') as file:  # file_name = Temp/temp.txt
#         for line in file:
#             print(line, end='')
# except OSError as error:
#     print(f'Error is: {error}')
# finally:
#     print('\nfile read complete')

"""
Основні можливості pathlib
"""
# from pathlib import Path
# current_path = Path()
# print(current_path)
# print(current_path.cwd())
# file = current_path / 'bin' / 'image' / 'test.png'
# print(file)
# file = current_path.joinpath('bin', 'image', 'test.drawio.svg')
# print(file)

# print(file.parts)

# print(file.name)
# print(file.name.split('.')[2])

# print(file.parent)
# print(file.suffix)
# print(file.suffixes)

"""
Більше можливостей pathlib
"""
# from pathlib import Path
# current_dir = Path('.')
# print(current_dir)
# # current_dir = current_dir / 'Temp'
# file = current_dir / 'bin' / 'image' / 'test.png'
# # print(file.exists())

# for element in current_dir.glob('**/*.png'):
# # for element in current_dir.glob('*.txt'):
#     print(element)

# tmp = Path('empty.txt')
# if tmp.exists():
#     tmp.unlink()

"""
Створення директорій pathlib
"""
# from pathlib import Path
# new_dir = Path('Hello')
# new_dir.mkdir(exist_ok=True)
# new_dir.rmdir()
# new_dir = Path('Hello/world/test')
# new_dir.mkdir(exist_ok=True, parents=True)

"""
Запис у файл байтових рядків. Робота з різними кодуваннями
"""
# from pathlib import Path
# text = 'Привіт потік GoIT 19!'
# print(text.encode())
# print(text.encode('utf-16'))
# print(text.encode('cp1251'))
# a = b'\xcf\xf0\xe8\xe2\xb3\xf2 \xef\xee\xf2\xb3\xea GoIT 19!'
# print(a.decode('cp1251'))
# folder = Path('Hello')
# with open(folder / 'utf-8.txt', 'wb') as f:
#     f.write(text.encode())
# with open(folder / 'utf-16.txt', 'wb') as f:
#     f.write(text.encode('utf-16'))
# with open(folder / 'cp1251.txt', 'wb') as f:
#     f.write(text.encode('cp1251'))


# with open(folder / 'utf-8.txt', 'rb') as f:
#     print(f.read().decode())
# with open(folder / 'utf-16.txt', 'rb') as f:
#     print(f.read().decode('utf-16'))
# with open(folder / 'cp1251.txt', 'rb') as f:
#     print(f.read().decode('cp1251'))

"""
Робота з архівами
"""
# import shutil
# print(shutil.get_archive_formats())
# archive = shutil.make_archive('archive_file_name', 'zip', 'Hello')
# print(archive)  # /Users/vova/PycharmProjects/GoIT19/lesson_6/archive_file_name.zip

# shutil.unpack_archive(archive, 'Archive/Test/In')
'''
Заархівовування
'''
# import shutil

# shutil.make_archive('archive', 'zip', 'test/')
# # 'archive' - назва файлу архіву
# # 'zip' - тип архіву
# # 'test/' - папка яку потрібно заархівувати
'''
Розархівовування
'''
# import shutil
# shutil.unpack_archive('archive.zip', 'dir/')  # dir - назва директорії куди потрібно розархівувати
# shutil.rmtree('dir/archives')                 # - видаляє непусту папку
# shutil.move('archive', 'dir')                 # - переміщає файл 'archive' в папку 'dir'
# shutil.copy('text.txt', 'dir/')               # - копіює файл 'text.txt' в папку 'dir'

