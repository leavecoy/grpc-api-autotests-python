"""Модели данных упражнения для тестовых фикстур."""

from pydantic import BaseModel, ConfigDict
from v1.exercises_pb2 import CreateExerciseRequest, GetExerciseResponse


class ExerciseFixture(BaseModel):
    """Хранит запрос на создание упражнения и ответ сервиса."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: CreateExerciseRequest
    response: GetExerciseResponse

    @property
    def exercise_id(self) -> str:
        """Возвращает идентификатор созданного упражнения.

        Returns:
            Идентификатор упражнения из ответа сервиса.
        """
        return self.response.exercise.id
