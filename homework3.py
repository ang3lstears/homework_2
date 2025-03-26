print('number 1')
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance
    @staticmethod
    def check_positive_amount(amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом.")
    def deposit(self, amount):
        self.check_positive_amount(amount)
        self.__balance += amount
    def withdraw(self, amount):
        self.check_positive_amount(amount)
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счёте.")
        self.__balance -= amount
    def get_balance(self):
        return self.__balance
    @classmethod
    def create_empty_account(cls, account_number):
        return cls(account_number)
acc = BankAccount.create_empty_account("123456789")
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())
print('number 2')
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    @staticmethod
    def check_password_complexity(password):
        if len(password) < 6:
            raise ValueError("Пароль должен содержать не менее 6 символов.")
    @classmethod
    def create_default_user(cls, username):
        default_password = "SecurePass123"
        return cls(username, default_password)
    def set_password(self, new_password):
        self.check_password_complexity(new_password)
        self.__password = new_password
        print("Пароль успешно изменён.")
    def get_username(self):
        return self.__username
user = User.create_default_user("Alice")
print(user.get_username())
#user.set_password("12345")
user.set_password("securePass")
print('number 3')
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.__title = title
        self.__author = author
        self.set_year(year)
    @staticmethod
    def check_year(year: int) -> bool:
        from datetime import datetime
        current_year = datetime.now().year
        if not isinstance(year, int) or year > current_year:
            raise ValueError("Год издания должен быть целым числом и не в будущем.")
        return True
    @classmethod
    def create_default_year(cls, title: str, author: str):
        return cls(title, author, 2024)
    def set_year(self, year: int):
        self.check_year(year)
        self.__year = year
    def get_info(self) -> str:
        return f"{self.__title}, автор: {self.__author}, год: {self.__year}"
book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())
book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
print(book2.get_info())
