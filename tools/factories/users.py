"""Фабрика запросов на создание пользователей."""

from typing import Callable

from v1.users_pb2 import CreateUserRequest

from tools.fakers import Fake, fake


class UserFactory:
    """Формирует запросы на создание пользователей с тестовыми данными."""

    def __init__(self, fake_generator: Fake):
        """Инициализирует фабрику запросов.

        Args:
            fake_generator: Генератор случайных данных пользователя.
        """
        self.fake = fake_generator

    @staticmethod
    def _resolve(value: str | None, default_factory: Callable[[], str]) -> str:
        """Подставляет сгенерированное значение, если передано None.

        Args:
            value: Заданное значение или None.
            default_factory: Функция генерации значения по умолчанию.

        Returns:
            Переданное значение или результат вызова генератора.
        """
        return default_factory() if value is None else value

    def create_user_request(
        self,
        email: str | None = None,
        password: str | None = None,
        last_name: str | None = None,
        first_name: str | None = None,
        middle_name: str | None = None,
    ) -> CreateUserRequest:
        """Формирует запрос на создание пользователя, генерируя незаданные поля.

        Args:
            email: Адрес электронной почты или None для генерации.
            password: Пароль или None для генерации.
            last_name: Фамилия или None для генерации.
            first_name: Имя или None для генерации.
            middle_name: Отчество или None для генерации.

        Returns:
            Protobuf-запрос на создание пользователя.
        """

        request = CreateUserRequest(
            email=self._resolve(email, self.fake.email),
            password=self._resolve(password, self.fake.password),
            last_name=self._resolve(last_name, self.fake.last_name),
            first_name=self._resolve(first_name, self.fake.first_name),
            middle_name=self._resolve(middle_name, self.fake.middle_name),
        )

        return request


user_factory = UserFactory(fake_generator=fake)
