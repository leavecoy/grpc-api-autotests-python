"""Тестовые сценарии использования фикстур."""

from clients.courses.courses_client import CoursesClient
from fixtures.authentication import AuthMetadata
from fixtures.users import UserFixture


def test_function_user(function_user: UserFixture):
    """Выводит данные пользователя, созданного фикстурой.

    Args:
        function_user: Данные созданного тестового пользователя.
    """
    print(function_user)


def test_authorized_user(auth_metadata: AuthMetadata):
    """Выводит метаданные аутентификации тестового пользователя.

    Args:
        auth_metadata: Метаданные аутентификации тестового пользователя.
    """
    print(auth_metadata.metadata)


def test_courses_client(courses_client: CoursesClient):
    """Вызывает создание курса через клиент из фикстуры.

    Args:
        courses_client: Клиент сервиса курсов с метаданными аутентификации.
    """
    courses_client.create_course(
        title="title",
        description="desc",
        preview_file_id="7f6e0b47-0e7c-4f7b-8e44-7c3f1d0d7f2a",
        created_by_user_id="7f6e0b47-0e7c-4f7b-8e44-7c3f1d0d7f2a",
    )
