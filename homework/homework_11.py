# ЗАДАНИЕ 1: Класс Book (Книга)

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return True if int(self.pages) > 300 else False


my_book_1 = Book("Учебник Python", "Иван Иваныч", 700)
my_book_2 = Book("Финтех", "Олег Деньгович", 100)
my_book_3 = Book("Будущее делается сегодня", "Инфо Продаваныч", 299)

print(my_book_1.get_info(), my_book_1.is_long())
print(my_book_2.get_info(), my_book_2.is_long())
print(my_book_3.get_info(), my_book_3.is_long())


# ЗАДАНИЕ 2: Класс BankAccount (Банковский счёт)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


bank_account = BankAccount("Ломакин Владисла", 1000)
bank_account.deposit(500)
print(bank_account.withdraw(299))
print(bank_account.withdraw(2000))
print(bank_account.get_balance())
