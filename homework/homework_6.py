# ЗАДАНИЕ 1: Работа со словарями и перебор элементов

my_dict = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2,
    "город": "Москва"
}

print(my_dict.keys())
print(my_dict.values())

print("=" * 30)

for key, value in my_dict.items():
    print(f"{key}: {value}")

print("=" * 30)

for value in my_dict.values():
    print(value)

# ЗАДАНИЕ 2: Удаление элементов и генератор словарей
print("=" * 30)
print("Задание 2")

prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}

del prices["груша"]
grape = prices.pop("виноград")

prices_with_discount = {key: value * 0.9 for key, value in prices.items()}

print(f"Словарь prices: {prices}")
print(f"Переменная grape: {grape}")
print(f"Словарь prices_with_discount: {prices_with_discount}")

# ЗАДАНИЕ 3: Объединение словарей
print("=" * 30)
print("Задание 3")

student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}

student1.update(student2)
print(student1)

student3 = {**student1, **student2}
print(f"student1: {student1}")
print(f"student2: {student2}")
print(f"student3: {student3}")
