"""Фабрика запросов на создание упражнений."""

from uuid import UUID

from v1.exercises_pb2 import CreateExerciseRequest

from tools.factories.base_factory import BaseFactory
from tools.fakers import Fake, fake


class ExercisesFactory(BaseFactory):
    """Формирует запросы на создание упражнений с тестовыми данными."""

    def __init__(self, fake_generator: Fake):
        """Инициализирует фабрику запросов.

        Args:
            fake_generator: Генератор случайных тестовых данных.
        """
        super().__init__(fake_generator)
        self.fake = fake_generator

    def create_exercise_request(
        self,
        title: str | None = None,
        course_id: UUID | str | None = None,
        max_score: int | None = None,
        min_score: int | None = None,
        order_index: int | None = None,
        description: str | None = None,
        estimated_time: str | None = None,
    ) -> CreateExerciseRequest:
        """Формирует запрос на создание упражнения, генерируя незаданные поля.

        Args:
            title: Название упражнения или None для генерации.
            course_id: Идентификатор курса в виде UUID или строки либо None
                для генерации UUID.
            max_score: Максимальный балл или None для генерации от 11 до 20.
            min_score: Минимальный балл или None для генерации от 0 до 10.
            order_index: Порядковый номер упражнения или None для генерации
                от 0 до 100.
            description: Описание упражнения или None для генерации.
            estimated_time: Ожидаемое время выполнения или None для генерации.

        Returns:
            Protobuf-запрос на создание упражнения.
        """

        request = CreateExerciseRequest(
            title=self._resolve(title, self.fake.text),
            course_id=str(self._resolve(course_id, self.fake.uuid)),
            max_score=self._resolve(max_score, self.fake.max_score),
            min_score=self._resolve(min_score, self.fake.min_score),
            order_index=self._resolve(order_index, self.fake.integer),
            description=self._resolve(description, self.fake.text),
            estimated_time=self._resolve(estimated_time, self.fake.estimated_time),
        )

        return request


exercises_factory = ExercisesFactory(fake_generator=fake)
