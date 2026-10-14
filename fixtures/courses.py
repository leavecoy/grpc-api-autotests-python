"""Фикстуры для создания тестовых курсов и их удаления после тестов."""

from typing import Any, Generator

import pytest
from v1.courses_pb2 import DeleteCourseRequest

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
) -> Generator[CourseFixture, Any, None]:
    """Создаёт курс с тестовыми данными и файлом превью из фикстуры.

    После завершения теста удаляет созданный курс.

    Args:
        function_user: Данные созданного тестового пользователя.
        function_file: Данные созданного файла превью курса.
        courses_client: Клиент сервиса курсов с метаданными аутентификации.

    Yields:
        Данные запроса на создание курса и ответ сервиса.
    """

    create_request = courses_factory.create_course_request(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id,
    )
    create_response = courses_client.create_course_api(create_request)

    yield CourseFixture(request=create_request, response=create_response)

    delete_request = DeleteCourseRequest(id=create_response.course.id)
    courses_client.delete_course_api(delete_request)
