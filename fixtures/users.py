"""Фикстуры для создания тестовых пользователей и их удаления после тестов."""

from typing import Any, Generator

import pytest
from grpc import Channel
from v1.users_pb2 import GetUserRequest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_models import AuthMetadata, Token
from clients.users.users_client import UsersClient
from clients.users.users_models import UserFixture
from tools.factories.users import users_factory


@pytest.fixture
def function_user(
    public_users_client,
    authentication_client: AuthenticationClient,
    grpc_channel: Channel,
) -> Generator[UserFixture, Any, None]:
    """Создаёт пользователя со случайными данными для теста.

    До передачи данных тесту выполняет вход созданного пользователя и готовит
    клиент с полученными метаданными аутентификации. После завершения теста
    удаляет пользователя через подготовленный клиент.

    Args:
        public_users_client: Клиент сервиса пользователей без метаданных аутентификации.
        authentication_client: Клиент сервиса аутентификации для входа до начала теста.
        grpc_channel: Канал для выполнения gRPC-запроса на удаление пользователя.

    Yields:
        Данные запроса на создание пользователя и ответ сервиса.
    """

    create_request = users_factory.create_user_request()
    create_response = public_users_client.create_user_api(create_request)

    login_response = authentication_client.login(
        email=create_request.email, password=create_request.password
    )
    auth_data = AuthMetadata(
        token=Token(
            token_type=login_response.token.token_type,
            access_token=login_response.token.access_token,
            refresh_token=login_response.token.refresh_token,
        ),
    )
    metadata = auth_data.metadata
    deleting_client = UsersClient(channel=grpc_channel, metadata=metadata)

    yield UserFixture(request=create_request, response=create_response)

    deleting_request = GetUserRequest(id=create_response.user.id)
    deleting_client.delete_user_api(deleting_request)
