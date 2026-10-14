"""Фабрика запросов на создание пользователей."""

from v1.users_pb2 import CreateUserRequest

from tools.factories.base_factory import BaseFactory
from tools.fakers import Fake, fake


class UserFactory(BaseFactory):
    """Формирует запросы на создание пользователей с тестовыми данными."""

    def __init__(self, fake_generator: Fake):
        """Инициализирует фабрику запросов.

        Args:
            fake_generator: Генератор случайных данных пользователя.
        """
        super().__init__(fake_generator)
        self.fake = fake_generator

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


users_factory = UserFactory(fake_generator=fake)
