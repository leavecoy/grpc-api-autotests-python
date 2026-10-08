"""Фикстуры метаданных аутентификации."""

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_models import AuthMetadata, Token
from fixtures.users import UserFixture


@pytest.fixture
def auth_metadata(
    function_user: UserFixture, authentication_client: AuthenticationClient
) -> AuthMetadata:
    """Выполняет вход тестового пользователя и формирует метаданные аутентификации.

    Args:
        function_user: Данные созданного тестового пользователя.
        authentication_client: Клиент сервиса аутентификации.

    Returns:
        Метаданные аутентификации с полученными токенами.
    """

    response = authentication_client.login(
        email=function_user.request.email, password=function_user.request.password
    )
    metadata = AuthMetadata(
        token=Token(
            token_type=response.token.token_type,
            access_token=response.token.access_token,
            refresh_token=response.token.refresh_token,
        )
    )

    return metadata
