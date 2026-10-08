"""Модели данных пользователя для тестовых фикстур."""

from pydantic import BaseModel, ConfigDict
from v1.users_pb2 import CreateUserRequest, GetUserResponse


class UserFixture(BaseModel):
    """Хранит запрос на создание пользователя и ответ сервиса."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: CreateUserRequest
    response: GetUserResponse

    @property
    def email(self) -> str:
        """Возвращает адрес электронной почты пользователя.

        Returns:
            Адрес электронной почты из запроса на создание пользователя.
        """
        return self.request.email

    @property
    def password(self) -> str:
        """Возвращает пароль пользователя.

        Returns:
            Пароль из запроса на создание пользователя.
        """
        return self.request.password

    @property
    def user_id(self) -> str:
        """Возвращает идентификатор созданного пользователя.

        Returns:
            Идентификатор пользователя из ответа сервиса.
        """
        return self.response.user.id
