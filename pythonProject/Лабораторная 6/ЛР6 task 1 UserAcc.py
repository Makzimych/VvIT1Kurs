class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Создание приватного атрибута c помощью __

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password

user = UserAccount('IvanovIvan', 'IvanovIvan@gmail.com', 'qwerty123')
user.set_password('ytrewq123')
is_correct = user.check_password('ytrewq123')
print(is_correct)  # True
is_correct = user.check_password('stepan228')
print(is_correct)  # False
