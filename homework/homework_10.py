# ЗАДАНИЕ 1: Функции и условия
# 1. Создайте функцию calculate_total(price, tax_percent):

def calculate_total(price, tax_percent):
    """Принимает price (float или int)
    и tax_percent - int в процентах, без знака "%"
    Например: если налог 15%, то передать нужно число 15"""

    if price < 0:
        return "Ошибка: цена не может быть меньше ноля"
    if tax_percent > 20:
        return "Ошибка: налог не может быть больше 20%"
    return price * (1 + tax_percent / 100)


# 2. Создайте функцию get_level(points):
#    - points >= 100 → "Эксперт"
#    - points >= 50 → "Продвинутый"
#    - points >= 20 → "Начинающий"
#    - иначе → "Новичок"

def get_level(points):
    if points >= 100:
        return "Эксперт"
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"


# ЗАДАНИЕ 2: Функции с условиями и match/case
# 1. Создайте функцию process_status(status) с match/case:

def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"
