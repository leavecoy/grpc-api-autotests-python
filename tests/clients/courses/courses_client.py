"""Тестовый gRPC-клиент для работы с курсами."""

from uuid import UUID

from grpc import Channel
from v1.common_pb2 import Empty
from v1.courses_pb2 import (
    CreateCourseRequest,
    DeleteCourseRequest,
    GetCourseRequest,
    GetCourseResponse,
    ListCoursesRequest,
    ListCoursesResponse,
    UpdateCourseRequest,
)
from v1.courses_pb2_grpc import CoursesServiceStub

from tests.clients.client import GRPCTestClient


class CoursesGRPCTestClient(GRPCTestClient):
    """Предоставляет методы создания, получения, обновления и удаления курсов."""

    def __init__(self, channel: Channel):
        """Инициализирует клиент и заглушку сервиса курсов.

        Args:
            channel: Канал для выполнения gRPC-запросов.
        """
        super().__init__(channel)

        self.stub = CoursesServiceStub(self.channel)

    def create_course_api(self, request: CreateCourseRequest) -> GetCourseResponse:
        """Вызывает RPC создания курса с готовым запросом.

        Args:
            request: Protobuf-запрос на создание курса.

        Returns:
            Ответ сервиса с созданным курсом.
        """

        return self.stub.CreateCourse(request)

    def create_course(
        self,
        title: str,
        description: str,
        preview_file_id: UUID,
        created_by_user_id: UUID,
        max_score: int | None = None,
        min_score: int | None = None,
        estimated_time: str | None = None,
    ) -> GetCourseResponse:
        """Формирует запрос и создаёт курс.

        Args:
            title: Название курса.
            description: Описание курса.
            preview_file_id: Идентификатор файла превью курса.
            created_by_user_id: Идентификатор пользователя, создающего курс.
            max_score: Максимальный балл за курс, если задан.
            min_score: Минимальный балл за курс, если задан.
            estimated_time: Ожидаемое время прохождения курса, если задано.

        Returns:
            Ответ сервиса с созданным курсом.
        """
        request = CreateCourseRequest(
            title=title,
            max_score=max_score,
            min_score=min_score,
            description=description,
            estimated_time=estimated_time,
            preview_file_id=str(preview_file_id),
            created_by_user_id=str(created_by_user_id),
        )
        response = self.create_course_api(request)

        return response

    def get_course_api(self, request: GetCourseRequest) -> GetCourseResponse:
        """Вызывает RPC получения курса с готовым запросом.

        Args:
            request: Protobuf-запрос на получение курса.

        Returns:
            Ответ сервиса с запрошенным курсом.
        """

        return self.stub.GetCourse(request)

    def get_course(self, course_id: UUID) -> GetCourseResponse:
        """Получает курс по его идентификатору.

        Args:
            course_id: Идентификатор курса.

        Returns:
            Ответ сервиса с запрошенным курсом.
        """

        request = GetCourseRequest(id=str(course_id))
        response = self.get_course_api(request)

        return response

    def list_courses_api(self, request: ListCoursesRequest) -> ListCoursesResponse:
        """Вызывает RPC получения списка курсов с готовым запросом.

        Args:
            request: Protobuf-запрос на получение списка курсов.

        Returns:
            Ответ сервиса со списком курсов.
        """

        return self.stub.ListCourses(request)

    def list_courses(self, user_id: UUID) -> ListCoursesResponse:
        """Получает список курсов для указанного пользователя.

        Args:
            user_id: Идентификатор пользователя для запроса списка курсов.

        Returns:
            Ответ сервиса со списком курсов.
        """

        request = ListCoursesRequest(user_id=str(user_id))
        response = self.list_courses_api(request)

        return response

    def update_course_api(self, request: UpdateCourseRequest) -> GetCourseResponse:
        """Вызывает RPC обновления курса с готовым запросом.

        Args:
            request: Protobuf-запрос на обновление курса.

        Returns:
            Ответ сервиса с обновлённым курсом.
        """

        return self.stub.UpdateCourse(request)

    def update_course(
        self,
        course_id: UUID,
        title: str | None = None,
        max_score: int | None = None,
        min_score: int | None = None,
        description: str | None = None,
        estimated_time: str | None = None,
    ) -> GetCourseResponse:
        """Формирует запрос и обновляет курс по его идентификатору.

        Args:
            course_id: Идентификатор обновляемого курса.
            title: Новое название курса, если задано.
            max_score: Новый максимальный балл, если задан.
            min_score: Новый минимальный балл, если задан.
            description: Новое описание курса, если задано.
            estimated_time: Новое ожидаемое время прохождения, если задано.

        Returns:
            Ответ сервиса с обновлённым курсом.
        """

        request = UpdateCourseRequest(
            id=str(course_id),
            title=title,
            max_score=max_score,
            min_score=min_score,
            description=description,
            estimated_time=estimated_time,
        )
        response = self.update_course_api(request)

        return response

    def delete_course_api(self, request: DeleteCourseRequest) -> Empty:
        """Вызывает RPC удаления курса с готовым запросом.

        Args:
            request: Protobuf-запрос на удаление курса.

        Returns:
            Пустой ответ сервиса после удаления курса.
        """

        return self.stub.DeleteCourse(request)

    def delete_course(self, course_id: UUID) -> Empty:
        """Удаляет курс по его идентификатору.

        Args:
            course_id: Идентификатор удаляемого курса.

        Returns:
            Пустой ответ сервиса после удаления курса.
        """

        request = DeleteCourseRequest(id=str(course_id))
        response = self.delete_course_api(request)

        return response
