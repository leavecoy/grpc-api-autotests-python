"""Генераторы случайных данных для тестов."""

from faker import Faker


class Fake:
    """Предоставляет методы генерации случайных данных пользователя."""

    def __init__(self, faker: Faker):
        """Инициализирует генератор тестовых данных.

        Args:
            faker: Экземпляр Faker для генерации случайных значений.
        """

        self.faker = faker

    def email(self) -> str:
        """Генерирует адрес электронной почты.

        Returns:
            Случайный адрес электронной почты.
        """
        return self.faker.email()

    def password(self) -> str:
        """Генерирует пароль.

        Returns:
            Случайный пароль.
        """
        return self.faker.password()

    def last_name(self) -> str:
        """Генерирует фамилию.

        Returns:
            Случайная фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """Генерирует имя.

        Returns:
            Случайное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """Генерирует значение для поля отчества на основе случайного имени.

        Returns:
            Случайное имя для использования в поле отчества.
        """
        return self.faker.first_name()


fake = Fake(faker=Faker())
