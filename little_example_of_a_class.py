import re
import random 
import string

class User:
    """Передаёт имя, совершеннолетний ли пользователь и генерирует пароль"""
    def __init__(self, name: str, age: int):
        """Создание пользователя, name - имя, age - возраст"""
        self.name = name
        self.age = age
    def is_adult(self) -> bool:
        """Вычисляет, совершеннолетний ли пользователь"""
        return self.age >= 18
    def generate_password(self, length: int) -> str:
        """Генерирует рандомный пароль"""
        self.length = length
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for i in range(self.length))
        return password
    def get_name(self) -> str:
        """Возвращает имя пользователя"""
        return self.name

