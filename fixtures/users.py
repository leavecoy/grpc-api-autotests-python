"""Фикстуры для создания тестовых пользователей."""

import pytest

from clients.users.users_client import UsersClient
from clients.users.users_models import UserFixture
from tools.factories.users import user_factory


@pytest.fixture
def function_user(public_users_client: UsersClient) -> UserFixture:
    """Создаёт пользователя со случайными данными для теста.

    Args:
        public_users_client: Клиент сервиса пользователей без метаданных аутентификации.

    Returns:
        Данные запроса на создание пользователя и ответ сервиса.
    """
    request = user_factory.create_user_request()
    response = public_users_client.create_user_api(request)

    return UserFixture(request=request, response=response)
