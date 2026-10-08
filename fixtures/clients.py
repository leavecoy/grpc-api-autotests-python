"""Фикстуры gRPC-канала и клиентов сервисов."""

import pytest
from grpc import Channel, insecure_channel

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_models import AuthMetadata
from clients.courses.courses_client import CoursesClient
from clients.exercises.exercises_client import ExercisesClient
from clients.files.files_client import FilesClient
from clients.users.users_client import UsersClient


@pytest.fixture
def grpc_channel():
    """Создаёт gRPC-канал и закрывает его после завершения теста.

    Yields:
        Канал для обращения к локальному gRPC-серверу.
    """
    channel = insecure_channel("localhost:9000")

    yield channel

    channel.close()


@pytest.fixture
def courses_client(grpc_channel: Channel, auth_metadata: AuthMetadata):
    """Создаёт клиент сервиса курсов.

    Args:
        grpc_channel: Канал для выполнения gRPC-запросов.
        auth_metadata: Метаданные аутентификации тестового пользователя.

    Returns:
        Клиент сервиса курсов.
    """
    return CoursesClient(channel=grpc_channel, metadata=auth_metadata.metadata)


@pytest.fixture
def public_users_client(grpc_channel: Channel):
    """Создаёт клиент сервиса пользователей без метаданных аутентификации.

    Args:
        grpc_channel: Канал для выполнения gRPC-запросов.

    Returns:
        Клиент сервиса пользователей без метаданных аутентификации.
    """
    return UsersClient(channel=grpc_channel)


@pytest.fixture
def private_users_client(grpc_channel: Channel, auth_metadata: AuthMetadata):
    """Создаёт клиент сервиса пользователей с метаданными аутентификации.

    Args:
        grpc_channel: Канал для выполнения gRPC-запросов.
        auth_metadata: Метаданные аутентификации тестового пользователя.

    Returns:
        Клиент сервиса пользователей с метаданными аутентификации.
    """
    return UsersClient(channel=grpc_channel, metadata=auth_metadata.metadata)


@pytest.fixture
def files_client(grpc_channel: Channel, auth_metadata: AuthMetadata):
    """Создаёт клиент сервиса файлов.

    Args:
        grpc_channel: Канал для выполнения gRPC-запросов.
        auth_metadata: Метаданные аутентификации тестового пользователя.

    Returns:
        Клиент сервиса файлов.
    """
    return FilesClient(channel=grpc_channel, metadata=auth_metadata.metadata)


@pytest.fixture
def exercises_client(grpc_channel: Channel, auth_metadata: AuthMetadata):
    """Создаёт клиент сервиса упражнений.

    Args:
        grpc_channel: Канал для выполнения gRPC-запросов.
        auth_metadata: Метаданные аутентификации тестового пользователя.

    Returns:
        Клиент сервиса упражнений.
    """
    return ExercisesClient(channel=grpc_channel, metadata=auth_metadata.metadata)


@pytest.fixture
def authentication_client(grpc_channel: Channel):
    """Создаёт клиент сервиса аутентификации.

    Args:
        grpc_channel: Канал для выполнения gRPC-запросов.

    Returns:
        Клиент сервиса аутентификации.
    """
    return AuthenticationClient(channel=grpc_channel)
