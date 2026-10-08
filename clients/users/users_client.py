"""Тестовый gRPC-клиент для работы с пользователями."""

from uuid import UUID

from grpc import Channel

from clients.types import GRPCMetadata
from v1.common_pb2 import Empty
from v1.users_pb2 import (
    CreateUserRequest,
    GetUserRequest,
    GetUserResponse,
    UpdateUserRequest,
)
from v1.users_pb2_grpc import UsersServiceStub

from clients.client import GRPCTestClient


class UsersClient(GRPCTestClient):
    """Предоставляет методы создания, получения, обновления и удаления пользователей."""

    def __init__(self, channel: Channel, metadata:GRPCMetadata | None = None):
        """Инициализирует клиент и заглушку сервиса пользователей.

        Args:
            channel: Канал для выполнения gRPC-запросов.
        """
        super().__init__(channel, metadata)

        self.stub = UsersServiceStub(self.channel)

    def create_user_api(self, request: CreateUserRequest) -> GetUserResponse:
        """Вызывает RPC создания пользователя с готовым запросом.

        Args:
            request: Protobuf-запрос на создание пользователя.

        Returns:
            Ответ сервиса с созданным пользователем.
        """

        return self.stub.CreateUser(request)

    def create_user(
        self,
        email: str,
        password: str,
        last_name: str,
        first_name: str,
        middle_name: str,
    ) -> GetUserResponse:
        """Формирует запрос и создаёт пользователя.

        Args:
            email: Адрес электронной почты пользователя.
            password: Пароль пользователя.
            last_name: Фамилия пользователя.
            first_name: Имя пользователя.
            middle_name: Отчество пользователя.

        Returns:
            Ответ сервиса с созданным пользователем.
        """

        request = CreateUserRequest(
            email=email,
            password=password,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
        )
        response = self.create_user_api(request)

        return response

    def update_user_api(self, request: UpdateUserRequest) -> GetUserResponse:
        """Вызывает RPC обновления пользователя с готовым запросом.

        Args:
            request: Protobuf-запрос на обновление пользователя.

        Returns:
            Ответ сервиса с обновлённым пользователем.
        """

        return self.call(self.stub.UpdateUser, request)

    def update_user(
        self,
        user_id: UUID,
        email: str | None = None,
        last_name: str | None = None,
        first_name: str | None = None,
        middle_name: str | None = None,
    ) -> GetUserResponse:
        """Формирует запрос и обновляет пользователя по его идентификатору.

        Args:
            user_id: Идентификатор обновляемого пользователя.
            email: Новый адрес электронной почты, если задан.
            last_name: Новая фамилия, если задана.
            first_name: Новое имя, если задано.
            middle_name: Новое отчество, если задано.

        Returns:
            Ответ сервиса с обновлённым пользователем.
        """
        request = UpdateUserRequest(
            id=str(user_id),
            email=email,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
        )
        response = self.update_user_api(request)

        return response

    def get_user_api(self, request: GetUserRequest) -> GetUserResponse:
        """Вызывает RPC получения пользователя с готовым запросом.

        Args:
            request: Protobuf-запрос на получение пользователя.

        Returns:
            Ответ сервиса с запрошенным пользователем.
        """

        return self.call(self.stub.GetUser, request)

    def get_user(self, user_id: UUID) -> GetUserResponse:
        """Получает пользователя по его идентификатору.

        Args:
            user_id: Идентификатор пользователя.

        Returns:
            Ответ сервиса с запрошенным пользователем.
        """

        request = GetUserRequest(id=str(user_id))
        response = self.get_user_api(request)

        return response

    def get_me_api(self, request: Empty) -> GetUserResponse:
        """Вызывает RPC получения текущего пользователя с готовым запросом.

        Args:
            request: Пустой Protobuf-запрос на получение текущего пользователя.

        Returns:
            Ответ сервиса с текущим пользователем.
        """

        return self.call(self.stub.GetMe, request)

    def get_me(self) -> GetUserResponse:
        """Формирует запрос и получает текущего пользователя.

        Returns:
            Ответ сервиса с текущим пользователем.
        """

        request = Empty()
        response = self.get_me_api(request)
        return response

    def delete_user_api(self, request: GetUserRequest) -> Empty:
        """Вызывает RPC удаления пользователя с готовым запросом.

        Args:
            request: Protobuf-запрос на удаление пользователя.

        Returns:
            Пустой ответ сервиса после удаления пользователя.
        """

        return self.call(self.stub.DeleteUser, request)

    def delete_user(self, user_id: UUID) -> Empty:
        """Удаляет пользователя по его идентификатору.

        Args:
            user_id: Идентификатор удаляемого пользователя.

        Returns:
            Пустой ответ сервиса после удаления пользователя.
        """

        request = GetUserRequest(id=str(user_id))
        response = self.delete_user_api(request)

        return response
