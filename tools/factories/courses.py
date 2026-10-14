"""Фабрика запросов на создание курсов."""

from uuid import UUID

from v1.courses_pb2 import CreateCourseRequest

from tools.factories.base_factory import BaseFactory
from tools.fakers import Fake, fake


class CoursesFactory(BaseFactory):
    """Формирует запросы на создание курсов с тестовыми данными."""

    def __init__(self, fake_generator: Fake):
        """Инициализирует фабрику запросов.

        Args:
            fake_generator: Генератор случайных тестовых данных.
        """
        super().__init__(fake_generator)
        self.fake = fake_generator

    def create_course_request(
        self,
        title: str | None = None,
        max_score: int | None = None,
        min_score: int | None = None,
        description: str | None = None,
        estimated_time: str | None = None,
        preview_file_id: UUID | None = None,
        created_by_user_id: UUID | None = None,
    ) -> CreateCourseRequest:
        """Формирует запрос на создание курса с тестовыми данными.

        Args:
            title: Название курса или None для генерации.
            max_score: Максимальный балл или None для генерации от 11 до 20.
            min_score: Минимальный балл или None для генерации от 0 до 10.
            description: Описание курса или None для генерации.
            estimated_time: Ожидаемое время прохождения или None для генерации.
            preview_file_id: Идентификатор файла превью, преобразуемый в строку.
                В текущей реализации None преобразуется в строку "None".
            created_by_user_id: Идентификатор создателя курса, преобразуемый
                в строку. В текущей реализации None преобразуется в строку "None".

        Returns:
            Protobuf-запрос на создание курса.
        """
        request = CreateCourseRequest(
            title=self._resolve(title, fake.text),
            max_score=self._resolve(max_score, fake.max_score),
            min_score=self._resolve(min_score, fake.min_score),
            description=self._resolve(description, fake.text),
            estimated_time=self._resolve(estimated_time, fake.estimated_time),
            preview_file_id=self._resolve(str(preview_file_id), fake.uuid),
            created_by_user_id=self._resolve(str(created_by_user_id), fake.uuid),
        )

        return request


courses_factory = CoursesFactory(fake_generator=fake)

"""
  string title = 1;
  optional int32 max_score = 2;
  optional int32 min_score = 3;
  string description = 4;
  optional string estimated_time = 5;
  string preview_file_id = 6;
  string created_by_user_id = 7;
"""
