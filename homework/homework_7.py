# ЗАДАНИЕ 1: Работа с множествами

# Дано множество фруктов:
fruits = {"яблоко", "банан"}

fruits.add("апельсин")
fruits.update(["груша"], ["виноград"])
fruits.discard("банан")
fruits.discard("киви")
# fruits.remove("киви")
fruits.pop()
print(fruits)

# ЗАДАНИЕ 2: Работа с кортежами

coordinates = (10, 20, 30, 20, 10, 20, 40)

print(coordinates[0])
print(coordinates[-1])

# под индексом 1 элемент 2, а под индексом 4 элемент 5,
# но выводится до 4 включительно
print(coordinates[1:4])
thirty_in_coordinates = 30 in coordinates
twenty_number_index = coordinates.index(20)
count_twenty_number = coordinates.count(20)
count_fifty_number = coordinates.count(50)
print(len(coordinates))