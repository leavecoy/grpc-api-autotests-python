"""Фикстуры для создания тестовых упражнений."""

import pytest

from clients.courses.courses_models import CourseFixture
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_models import ExerciseFixture
from tools.factories.exercises import exercises_factory


@pytest.fixture
def function_exercise(
    function_course: CourseFixture, exercises_client: ExercisesClient
) -> ExerciseFixture:
    """Создаёт упражнение с тестовыми данными для курса из фикстуры.

    Args:
        function_course: Данные созданного тестового курса.
        exercises_client: Клиент сервиса упражнений с метаданными аутентификации.

    Returns:
        Данные запроса на создание упражнения и ответ сервиса.
    """

    request = exercises_factory.create_exercise_request(
        course_id=function_course.response.course.id
    )
    response = exercises_client.create_exercise_api(request)

    return ExerciseFixture(request=request, response=response)
