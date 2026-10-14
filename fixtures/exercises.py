"""Фикстуры для создания тестовых упражнений и их удаления после тестов."""

import pytest

from clients.courses.courses_models import CourseFixture
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_models import ExerciseFixture
from tools.factories.exercises import exercises_factory
from typing import Any, Generator
from v1.exercises_pb2 import DeleteExerciseRequest


@pytest.fixture
def function_exercise(
    function_course: CourseFixture, exercises_client: ExercisesClient
) -> Generator[ExerciseFixture, Any, None]:
    """Создаёт упражнение с тестовыми данными для курса из фикстуры.

    После завершения теста удаляет созданное упражнение.

    Args:
        function_course: Данные созданного тестового курса.
        exercises_client: Клиент сервиса упражнений с метаданными аутентификации.

    Yields:
        Данные запроса на создание упражнения и ответ сервиса.
    """

    create_request = exercises_factory.create_exercise_request(
        course_id=function_course.response.course.id
    )
    create_response = exercises_client.create_exercise_api(create_request)

    yield ExerciseFixture(request=create_request, response=create_response)

    delete_request = DeleteExerciseRequest(id=create_response.exercise.id)
    exercises_client.delete_exercise_api(delete_request)
