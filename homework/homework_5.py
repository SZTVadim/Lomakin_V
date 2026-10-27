# ЗАДАНИЕ 1: Добавление элементов в список
fruits = ["яблоко"]
fruits.append("апельсин")
fruits.append("груша")
fruits.insert(1, "виноград")

# ЗАДАНИЕ 2: Удаление элементов из списка
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
banana_var = fruits.pop()

# ЗАДАНИЕ 3: Поиск элементов в списке
fruits = ["яблоко", "банан", "апельсин", "банан"]
first_banana = fruits.index("банан")
banana_count = fruits.count("банан")

# ЗАДАНИЕ 4: Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()
print("Задание 4: ", numbers)

# ЗАДАНИЕ 5:
my_generator = [num ** 3 for num in range(1, 9)]
generator_minimum = min(my_generator)
generator_maximum = max(my_generator)
print("Задание 5: ", my_generator, generator_minimum, generator_maximum)

# ЗАДАНИЕ 6:
my_list = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
my_filtred_list = [n for n in my_list if n > 10]
filtred_lits_sum = sum(my_filtred_list)
print("Задание 6: ", my_filtred_list, filtred_lits_sum)

# ЗАДАНИЕ 7:
cities = ["москва", "санкт-петербург", "казань"]
cities_title = [city.title() for city in cities]
print("Задание 7: ", cities_title)
