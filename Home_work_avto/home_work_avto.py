''' № 1
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

''' № 2
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

''' № 3
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
# def read_employees_from_file(path):
#     fh = open(path, 'r')
#     line = []
#     while True:
#         for i in fh.readlines():
#             i = str(i).replace('\n', '')
#             line.append(i)
#             continue
#         fh.close()
#         return line

# print(read_employees_from_file('d:\IT\GoIT\Modul_6\Home_work_avto\worker_list.txt'))

''' № 4
Реалізуйте функцію add_employee_to_file(record, path), яка у файл (параметр path - шлях до файлу) буде додавати співробітника (параметр record) у вигляді рядка "Drake Mikelsson,19".
Вимоги:
параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
кожен запис у файл має починатися з нового рядка.
необхідно щоб стара інформація у файлі теж зберігалася, тому при роботі з файлом відкрийте файл у режимі 'a', додайте співробітника record у файл і закрийте його
ми поки що не використовуємо менеджер контексту with
'''
# def add_employee_to_file(record, path):

#     fh = open(path, 'a')
#     fh.write(record + '\n')

#     fh.close()
#     return fh

# print(add_employee_to_file("Drake Mikelsson,19", 'd:\IT\GoIT\Modul_6\Home_work_avto\worker_list.txt'))

''' № 5
Ми маємо таку структуру файлу:
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
Кожен запис складається з трьох частин і починається з нового рядка. Наприклад, для першого запису початок 60b90c1c13067a15887e1ae1 — це первинний ключ бази даних MongoDB. Він завжди містить 12 байтів або рівно 24 символи. Далі ми бачимо прізвисько кота Tayson та його вік 3. Всі частини запису розділені символом кома ,
Розробіть функцію get_cats_info(path), яка повертатиме список словників із даними котів у вигляді:
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
Параметри функції:
path - шлях до файлу
Вимоги:
прочитайте вміст файлу за допомогою режиму "r".
ми використовуємо менеджер контексту with
поверніть із функції список котів із файлу у потрібному форматі
'''

# def get_cats_info(path):
#     cat_dict = []
#     with open(path, 'r') as fh:
#         for el in fh:
#             list_1 = el.strip().split(',')
#             cat_dict.append({'id': list_1[0], 'name': list_1[1], 'age': list_1[2]})


#         return cat_dict


# print(get_cats_info('d:\IT\GoIT\Modul_6\Home_work_avto\cats_list.txt'))

''' № 6
Нагадаємо, що у 4 модулі ми для кулінарного блогу писали функцію format_ingredients, яка приймала на вхід список з інгредієнтами рецепта.
Ми продовжимо працювати в цьому напрямку та створимо функцію, яка шукатиме рецепт у файлі та повертатиме знайдений рецепт у вигляді словника певної форми.
У вас є файл, який містить рецепти у вигляді:
60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce
60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese
60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water
Кожен рецепт записаний з нового рядка (не забуваємо під час вирішення завдання про кінець рядка). Кожен запис починається з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта, а потім через кому, йде перелік інгредієнтів рецепта.
Вам необхідно реалізувати функцію, котра буде отримувати інформацію про рецепт у вигляді словника для кожної страви що шукається. Створіть функцію get_recipe(path, search_id), яка повертатиме словник для рецепта із зазначеним ідентифікатором MongoDB.
Де параметри функції:
path — шлях до файлу.
search_id — первинний ключ MongoDB для пошуку рецепта
Вимоги:
Використовуйте менеджер контексту with для читання з файлу
Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None
Приклад: для файлу, вказаного вище, виклик функції у вигляді
get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese і повернути результат у вигляді словника такої структури:
{
    "id": "60b90c3b13067a15887e1ae4",
    "name": "Watermelon Cucumber Salad",
    "ingredients": [
        "1 large seedless watermelon",
        "12 leaves fresh mint",
        "1 cup crumbled feta cheese",
    ],
}
'''
# def get_recipe(path, search_id):
#     recipe = None
#     with open(path, 'r') as fh:
#         for el in fh:
#             recipe_1 = el.strip().split(',')
#             if recipe_1[0] == search_id:
#                 recipe = ({'id': recipe_1[0], 'name': recipe_1[1], 'ingredients': recipe_1[2:]})
#                 break
#     return recipe
 
# print(get_recipe('d:\IT\GoIT\Modul_6\Home_work_avto\culinary.txt', "60b90c2e13067a15887e1ae5"))

''' № 7
Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.
Вимоги:
прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write
'''
# import re

# def sanitize_file(source, output):
#     text = ''
#     with open(source, 'r') as fh_r:
#         text_r = fh_r.read()
#         text += re.sub(r'\d', '', (text_r))
        
#         with open(output, 'w') as fh_w:
#             fh_w = fh_w.write(text)
#             return text

# print(sanitize_file('d:\IT\GoIT\Modul_6\Home_work_avto\source.txt', 'd:\IT\GoIT\Modul_6\Home_work_avto\output.txt'))

''' № 8
Задано відомість абітурієнтів, які склали вступні іспити до університету. Структура даних щодо абітурієнтів подана у вигляді наступного списку:
[
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
У кожному словнику цього списку записано прізвище абітурієнта — ключ name, код спеціальності, на яку він поступив — ключ specialty, та отримані ним бали з окремих дисциплін — ключі math (математика), lang ( українська мова) та eng (англійська мова)
Розробіть функцію save_applicant_data(source, output), яка буде вказаний список із параметра source зберігати у файл із параметра output
Структура файлу для зберігання повинна бути наступною. У кожному новому рядку файлу повинні бути записані через кому без прогалин прізвище абітурієнта, код спеціальності, на яку він поступив, та отримані ним бали за окремими дисциплінами.
Kovalchuk Oleksiy,301,175,180,155
Ivanchuk Boryslav,101,135,150,165
Karpenko Dmitro,201,155,175,185
Вимоги:
відкрийте файл output для запису, використовуючи менеджер контексту with та режим w.
запис нового вмісту файлу output має бути або за допомогою методу writelines, або використовувати метод write
'''
# def save_applicant_data(source, output):
#     with open(output, 'w') as fh_w:
#         for el in source:
#             new_line = (f'{el["name"]},{el["specialty"]},{el["math"]},{el["lang"]},{el["eng"]}\n')
#             print(new_line)
#             fh_w.write(new_line)

# print(save_applicant_data([
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ], 'd:\IT\GoIT\Modul_6\Home_work_avto\output.txt'))

''' № 9
Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.
Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.
'''
# def is_equal_string(utf8_string, utf16_string):
#     utf8_string_norm = utf8_string.decode('utf-8').casefold()
#     utf16_string_norm = utf16_string.decode('utf-16').casefold()
#     if utf8_string_norm == utf16_string_norm:
#         return True
#     else:
#         return False
# #№ Варіант 2    
# def is_equal_string(utf8_string, utf16_string):
#     value = utf8_string.decode('utf-8').casefold() == utf16_string.decode('utf-16').casefold()
#     return value

''' № 10
Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями в бінарний файл.
Де:
path – шлях до файлу.
users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, де ключ — логін (username) користувача, а значення — його пароль (password).
Вимоги:
Кожен рядок файлу повинен мати такий вигляд username:password. Такий формат запису використовують при Базовій аутентифікації.
Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого рядка username:password для кожного елемента словника users_info
'''
# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as fh:
#         for username, password in users_info.items():
#             users_info = f'{username}:{password}\n'.encode('utf-8')
#             fh.write(users_info)

# print(save_credentials_users('username_password.bin', {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}))

''' № 11
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:
path – шлях до файлу.
Формат файлу:
andry:uyro18890D
steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:
['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:
Використовуйте менеджер контексту для читання з файлу
'''
# def get_credentials_users(path):
#     credentials_list = []
#     with open(path, 'rb') as fh:
#         for line in fh:
#             fh_str = line.decode('utf-8').strip()
#             credentials_list.append(fh_str)
#         return credentials_list
 
# print(get_credentials_users('username_password.bin'))

''' № 12
Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:
['andry:uyro18890D', 'steve:oppjM13LL9e']
Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:
['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
'''
# import base64

# def encode_data_to_base64(data):
#     data_list = []
#     for el in data:
#         message_bytes = el.encode("utf-8")
#         base64_bytes = base64.b64encode(message_bytes)
#         base64_message = base64_bytes.decode("utf-8")
#         data_list.append(base64_message)

#     return data_list     

# print(encode_data_to_base64(['andry:uyro18890D', 'steve:oppjM13LL9e']))

''' № 13
Реалізуйте функцію create_backup(path, file_name, employee_residence)
Де:
path — шлях до файлу
file_name — ім'я файлу
employee_residence — словник, у якому ключ — ім'я користувача, а значення — країна проживання. Вигляд: {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
Функція повинна працювати так:
Створювати бінарний файл file_name за шляхом path
Зберігати дані словника employee_residence у файл, де кожен новий рядок — це ключ значення через пробіл як "Michael Canada"
Архівувати теку по шляху path за допомогою shutil
Ім'я архіву має бути backup_folder.zip
Функція має повернути рядок шляху до архіву backup_folder.zip
Вимоги:
запишіть вміст словника employee_residence у бінарний файл з ім'ям file_name у теку path за допомогою оператора with.
використовуйте символ /, щоб розділити шлях для path та file_name
вигляд рядка файлу — Michael Canada, в кінці кожного рядка додається перенесення рядка '\n'.
при збереженні кожен рядок файлу кодується методом encode
при записі рядків використовуємо лише метод write
архів має бути у форматі zip з ім'ям 'backup_folder', створений за допомогою make_archive.
'''
# import shutil

# def create_backup(path, file_name, employee_residence):
#     with open(f"{path}/{file_name}", "wb") as file_withlist:
#         for employee, residence in employee_residence.items(): 
#             line = f"{employee} {residence}\n"
#             file_withlist.write(line.encode())
#         archive = shutil.make_archive("backup_folder", 'zip', path)
#         return archive

# print(create_backup('d:\IT\GoIT\Modul_6\Home_work_avto', 'employee_residence.bin',{'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}))

''' № 14
Створіть функціонал для розпакування архіву.
Зробіть import пакету shutil
Створіть функцію unpack(archive_path, path_to_unpack), яка викликатиме метод пакета shutil unpack_archive та розпаковуватиме архів archive_path у місце path_to_unpack.
Функція нічого не повертає.
'''
# import shutil

# def unpack(archive_path, path_to_unpack):
#     shutil.unpack_archive(archive_path, path_to_unpack)

                    

