"""Тестовый gRPC-клиент для работы с упражнениями."""

from uuid import UUID

from grpc import Channel
from v1.common_pb2 import Empty
from v1.exercises_pb2 import (
    CreateExerciseRequest,
    DeleteExerciseRequest,
    GetExerciseRequest,
    GetExerciseResponse,
    ListExercisesRequest,
    ListExercisesResponse,
    UpdateExerciseRequest,
)
from v1.exercises_pb2_grpc import ExercisesServiceStub

from clients.client import GRPCTestClient
from clients.types import GRPCMetadata


class ExercisesClient(GRPCTestClient):
    """Предоставляет методы создания, получения, обновления и удаления упражнений."""

    def __init__(self, channel: Channel, metadata: GRPCMetadata):
        """Инициализирует клиент и заглушку сервиса упражнений.

        Args:
            channel: Канал для выполнения gRPC-запросов.
            metadata: Метаданные для выполнения gRPC-запросов.
        """
        super().__init__(channel, metadata)

        self.stub = ExercisesServiceStub(self.channel)

    def create_exercise_api(
        self, request: CreateExerciseRequest
    ) -> GetExerciseResponse:
        """Вызывает RPC создания упражнения с готовым запросом.

        Args:
            request: Protobuf-запрос на создание упражнения.

        Returns:
            Ответ сервиса с созданным упражнением.
        """

        return self.call(self.stub.CreateExercise, request)

    def create_exercise(
        self,
        title: str,
        course_id: UUID,
        order_index: int,
        description: str,
        max_score: int | None = None,
        min_score: int | None = None,
        estimated_time: str | None = None,
    ) -> GetExerciseResponse:
        """Формирует запрос и создаёт упражнение.

        Args:
            title: Название упражнения.
            course_id: Идентификатор курса.
            order_index: Порядковый номер упражнения в курсе.
            description: Описание упражнения.
            max_score: Максимальный балл за упражнение, если задан.
            min_score: Минимальный балл за упражнение, если задан.
            estimated_time: Ожидаемое время выполнения упражнения, если задано.

        Returns:
            Ответ сервиса с созданным упражнением.
        """
        request = CreateExerciseRequest(
            title=title,
            course_id=str(course_id),
            max_score=max_score,
            min_score=min_score,
            order_index=order_index,
            description=description,
            estimated_time=estimated_time,
        )

        response = self.create_exercise_api(request)

        return response

    def get_exercise_api(self, request: GetExerciseRequest) -> GetExerciseResponse:
        """Вызывает RPC получения упражнения с готовым запросом.

        Args:
            request: Protobuf-запрос на получение упражнения.

        Returns:
            Ответ сервиса с запрошенным упражнением.
        """

        return self.call(self.stub.GetExercise, request)

    def get_exercise(self, exercise_id: UUID) -> GetExerciseResponse:
        """Получает упражнение по его идентификатору.

        Args:
            exercise_id: Идентификатор упражнения.

        Returns:
            Ответ сервиса с запрошенным упражнением.
        """

        request = GetExerciseRequest(id=str(exercise_id))
        response = self.get_exercise_api(request)

        return response

    def list_exercises_api(
        self, request: ListExercisesRequest
    ) -> ListExercisesResponse:
        """Вызывает RPC получения списка упражнений с готовым запросом.

        Args:
            request: Protobuf-запрос на получение списка упражнений.

        Returns:
            Ответ сервиса со списком упражнений.
        """

        return self.call(self.stub.ListExercises, request)

    def list_exercises(self, course_id: UUID) -> ListExercisesResponse:
        """Получает список упражнений для указанного курса.

        Args:
            course_id: Идентификатор курса для запроса списка упражнений.

        Returns:
            Ответ сервиса со списком упражнений.
        """

        request = ListExercisesRequest(course_id=str(course_id))
        response = self.list_exercises_api(request)
        return response

    def update_exercise_api(
        self, request: UpdateExerciseRequest
    ) -> GetExerciseResponse:
        """Вызывает RPC обновления упражнения с готовым запросом.

        Args:
            request: Protobuf-запрос на обновление упражнения.

        Returns:
            Ответ сервиса с обновлённым упражнением.
        """

        return self.call(self.stub.UpdateExercise, request)

    def update_exercise(
        self,
        exercise_id: UUID,
        title: str | None = None,
        max_score: int | None = None,
        min_score: int | None = None,
        order_index: int | None = None,
        description: str | None = None,
        estimated_time: str | None = None,
    ) -> GetExerciseResponse:
        """Формирует запрос и обновляет упражнение по его идентификатору.

        Args:
            exercise_id: Идентификатор обновляемого упражнения.
            title: Новое название упражнения, если задано.
            max_score: Новый максимальный балл, если задан.
            min_score: Новый минимальный балл, если задан.
            order_index: Новый порядковый номер упражнения, если задан.
            description: Новое описание упражнения, если задано.
            estimated_time: Новое ожидаемое время выполнения, если задано.

        Returns:
            Ответ сервиса с обновлённым упражнением.
        """

        request = UpdateExerciseRequest(
            id=str(exercise_id),
            title=title,
            max_score=max_score,
            min_score=min_score,
            order_index=order_index,
            description=description,
            estimated_time=estimated_time,
        )

        response = self.update_exercise_api(request)

        return response

    def delete_exercise_api(self, request: DeleteExerciseRequest) -> Empty:
        """Вызывает RPC удаления упражнения с готовым запросом.

        Args:
            request: Protobuf-запрос на удаление упражнения.

        Returns:
            Пустой ответ сервиса после удаления упражнения.
        """

        return self.call(self.stub.DeleteExercise, request)

    def delete_exercise(self, exercise_id: UUID) -> Empty:
        """Удаляет упражнение по его идентификатору.

        Args:
            exercise_id: Идентификатор удаляемого упражнения.

        Returns:
            Пустой ответ сервиса после удаления упражнения.
        """

        request = DeleteExerciseRequest(id=str(exercise_id))
        response = self.delete_exercise_api(request)

        return response
