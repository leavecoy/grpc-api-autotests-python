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


def test_function_file(function_file):
    """Выводит ответ сервиса с файлом, созданным фикстурой.

    Args:
        function_file: Данные созданного тестового файла.
    """
    print(function_file.response)


def test_function_course(function_course):
    """Выводит ответ сервиса с курсом, созданным фикстурой.

    Args:
        function_course: Данные созданного тестового курса.
    """
    print(function_course.response)


def test_function_exercise(function_exercise):
    """Выводит ответ сервиса с упражнением, созданным фикстурой.

    Args:
        function_exercise: Данные созданного тестового упражнения.
    """

    print(function_exercise.response)
