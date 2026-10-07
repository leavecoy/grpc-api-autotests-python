"""Тестовый gRPC-клиент для аутентификации и обновления токенов."""

from grpc import Channel
from v1.authentication_pb2 import LoginRequest, LoginResponse, RefreshRequest
from v1.authentication_pb2_grpc import AuthenticationServiceStub

from clients.client import GRPCTestClient


class AuthenticationClient(GRPCTestClient):
    """Предоставляет методы входа пользователя и обновления токенов."""

    def __init__(self, channel: Channel):
        """Инициализирует клиент и заглушку сервиса аутентификации.

        Args:
            channel: Канал для выполнения gRPC-запросов.
        """

        super().__init__(channel)

        self.stub = AuthenticationServiceStub(self.channel)

    def login_api(self, request: LoginRequest) -> LoginResponse:
        """Вызывает RPC входа пользователя с готовым запросом.

        Args:
            request: Protobuf-запрос на вход пользователя.

        Returns:
            Ответ сервиса с токенами аутентификации.
        """

        return self.stub.Login(request)

    def login(self, email: str, password: str) -> LoginResponse:
        """Формирует запрос и выполняет вход пользователя.

        Args:
            email: Адрес электронной почты пользователя.
            password: Пароль пользователя.

        Returns:
            Ответ сервиса с токенами аутентификации.
        """

        request = LoginRequest(email=email, password=password)
        response = self.login_api(request)

        return response

    def refresh_api(self, request: RefreshRequest) -> LoginResponse:
        """Вызывает RPC обновления токенов с готовым запросом.

        Args:
            request: Protobuf-запрос на обновление токенов.

        Returns:
            Ответ сервиса с обновлёнными токенами аутентификации.
        """

        return self.stub.Refresh(request)

    def refresh(self, refresh_token: str) -> LoginResponse:
        """Формирует запрос и обновляет токены аутентификации.

        Args:
            refresh_token: Токен обновления.

        Returns:
            Ответ сервиса с обновлёнными токенами аутентификации.
        """

        request = RefreshRequest(refresh_token=refresh_token)
        response = self.refresh_api(request)

        return response
