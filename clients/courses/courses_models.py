"""Модели данных курса для тестовых фикстур."""

from pydantic import BaseModel, ConfigDict
from v1.courses_pb2 import CreateCourseRequest, GetCourseResponse


class CourseFixture(BaseModel):
    """Хранит запрос на создание курса и ответ сервиса."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: CreateCourseRequest
    response: GetCourseResponse

    @property
    def course_id(self) -> str:
        """Возвращает идентификатор созданного курса.

        Returns:
            Идентификатор курса из ответа сервиса.
        """
        return self.response.course.id
