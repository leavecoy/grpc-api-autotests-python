"""Фикстуры для создания тестовых курсов."""

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_models import CourseFixture
from clients.files.files_models import FileFixture
from clients.users.users_models import UserFixture
from tools.factories.courses import courses_factory


@pytest.fixture
def function_course(
    function_user: UserFixture,
    function_file: FileFixture,
    courses_client: CoursesClient,
) -> CourseFixture:
    """Создаёт курс с тестовыми данными и файлом превью из фикстуры.

    Args:
        function_user: Данные созданного тестового пользователя.
        function_file: Данные созданного файла превью курса.
        courses_client: Клиент сервиса курсов с метаданными аутентификации.

    Returns:
        Данные запроса на создание курса и ответ сервиса.
    """

    request = courses_factory.create_course_request(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id,
    )
    response = courses_client.create_course_api(request)

    return CourseFixture(request=request, response=response)
