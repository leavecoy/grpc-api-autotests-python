"""Генераторы случайных данных для тестов."""

from faker import Faker


class Fake:
    """Предоставляет методы генерации случайных данных для тестов."""

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

    def text(self) -> str:
        """Генерирует короткий случайный текст.

        Returns:
            Случайный текст длиной не более 10 символов.
        """

        return self.faker.text(max_nb_chars=10)

    def filename(self) -> str:
        """Формирует имя файла с расширением PNG.

        Returns:
            Имя файла с расширением .png.
        """
        return f"{self.faker.uuid4()}.png"

    def min_score(self) -> int:
        """Генерирует минимальный балл.

        Returns:
            Случайное целое число от 0 до 10 включительно.
        """
        return self.faker.random_int(min=0, max=10)

    def max_score(self) -> int:
        """Генерирует максимальный балл.

        Returns:
            Случайное целое число от 11 до 20 включительно.
        """
        return self.faker.random_int(min=11, max=20)

    def estimated_time(self) -> str:
        """Генерирует ожидаемое время прохождения.

        Returns:
            Строка с числом от 1 до 20 и единицей времени days, weeks или months.
        """
        return f"{self.faker.random_int(min=1, max=20)} {self.faker.random_element(elements=["days", "weeks","months"])}"

    def uuid(self) -> str:
        """Генерирует случайный UUID версии 4.

        Returns:
            Строковое представление UUID.
        """
        return self.faker.uuid4()


fake = Fake(faker=Faker())
