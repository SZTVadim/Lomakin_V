# ЗАДАНИЕ 1: Работа с типами данных
# Создайте переменные разных типов и выведите их типы:

privet_string = "Привет"
forty_two = 42
pi_number = 3.14
my_list = [1, 2, 3]

print("ЗАДАНИЕ 1")
print(forty_two, pi_number, my_list, sep="\n")
print("=" * 60, end="\n\n")

# ЗАДАНИЕ 2: Преобразование регистра строк
# Дана строка: "python PROGRAMMING"

default_string = "python PROGRAMMING"
default_string_to_lower = default_string.lower()
default_string_to_upper = default_string.upper()
default_string_capitalize = default_string.capitalize()
default_string_title = default_string.title()

print("ЗАДАНИЕ 2")
print(default_string_to_lower, default_string_to_upper, default_string_capitalize, default_string_title, sep="\n")
print("=" * 60, end="\n\n")

# ЗАДАНИЕ 3: Удаление пробелов
# Дана строка с пробелами: "  Hello World  "

string_with_spaces = "  Hello World  "
string_with_spaces_strip = string_with_spaces.strip()
string_with_spaces_left_strip = string_with_spaces.lstrip()
string_with_spaces_right_strip = string_with_spaces.rstrip()

print("ЗАДАНИЕ 3")
print(string_with_spaces_strip, string_with_spaces_left_strip, string_with_spaces_right_strip, sep="\n")
print("=" * 60, end="\n\n")

# ЗАДАНИЕ 4: Разделение и объединение строк
# Дана строка: "яблоко,банан,апельсин,груша"

fruits_string = "яблоко,банан,апельсин,груша"
my_fruits_list = fruits_string.split(",")
my_fruits_string = " | ".join(my_fruits_list)

print("ЗАДАНИЕ 4")
print(my_fruits_list, my_fruits_string, sep="\n")
print("=" * 60, end="\n\n")

# ЗАДАНИЕ 5: Замена подстрок
# Дана строка: "Я изучаю Python. Python - это круто!"
python_love_string = "Я изучаю Python. Python - это круто!"
java_love_string = python_love_string.replace("Python", "Java")

print("ЗАДАНИЕ 5")
print(java_love_string)
print("=" * 60, end="\n\n")

# ЗАДАНИЕ 6: Поиск и подсчет
# Дана строка: "Python программирование на Python"

python_programming = "Python программирование на Python"
first_python_index = python_programming.index("Python")
python_count = python_programming.count("Python")
java_in_string = python_programming.find("Java")

print("ЗАДАНИЕ 6")
print(first_python_index, python_count, java_in_string, sep="\n")
print("=" * 60, end="\n\n")

# ЗАДАНИЕ 7: Проверка типа символов
print("ЗАДАНИЕ 7")
print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())
print("=" * 60, end="\n\n")

# ЗАДАНИЕ 8: Срезы строк
# Дана строка: "Python very good"
python_very_good = "Python very good"

print("ЗАДАНИЕ 8")
print(python_very_good[:3])
print(python_very_good[:-3])
print(python_very_good[::2])
print(python_very_good[::-1])
print("=" * 60, end="\n\n")

# ЗАДАНИЕ 9: Экранирование символов
print("ЗАДАНИЕ 9")
print("Он сказал: \"Привет\"")
print("Первая строка \nВторая строка")
