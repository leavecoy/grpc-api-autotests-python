"""Тестовый gRPC-клиент для работы с файлами."""

from uuid import UUID

from grpc import Channel
from v1.common_pb2 import Empty
from v1.files_pb2 import (
    CreateFileRequest,
    DeleteFileRequest,
    GetFileRequest,
    GetFileResponse,
)
from v1.files_pb2_grpc import FilesServiceStub

from clients.client import GRPCTestClient
from clients.types import GRPCMetadata


class FilesClient(GRPCTestClient):
    """Предоставляет методы создания, получения и удаления файлов."""

    def __init__(self, channel: Channel, metadata: GRPCMetadata):
        """Инициализирует клиент и заглушку сервиса файлов.

        Args:
            channel: Канал для выполнения gRPC-запросов.
            metadata: Метаданные для выполнения gRPC-запросов.
        """
        super().__init__(channel, metadata)
        self.stub = FilesServiceStub(self.channel)

    def create_file_api(self, request: CreateFileRequest) -> GetFileResponse:
        """Вызывает RPC создания файла с готовым запросом.

        Args:
            request: Protobuf-запрос на создание файла.

        Returns:
            Ответ сервиса с созданным файлом.
        """

        return self.call(self.stub.CreateFile, request)

    def create_file(
        self, filename: str, directory: str, content: bytes
    ) -> GetFileResponse:
        """Формирует запрос и создаёт файл.

        Args:
            filename: Имя файла.
            directory: Директория для сохранения файла.
            content: Содержимое файла в байтах.

        Returns:
            Ответ сервиса с созданным файлом.
        """

        request = CreateFileRequest(
            filename=filename, directory=directory, content=content
        )
        response = self.create_file_api(request)

        return response

    def get_file_api(self, request: GetFileRequest) -> GetFileResponse:
        """Вызывает RPC получения файла с готовым запросом.

        Args:
            request: Protobuf-запрос на получение файла.

        Returns:
            Ответ сервиса с запрошенным файлом.
        """

        return self.call(self.stub.GetFile, request)

    def get_file(self, file_id: UUID) -> GetFileResponse:
        """Получает файл по его идентификатору.

        Args:
            file_id: Идентификатор файла.

        Returns:
            Ответ сервиса с запрошенным файлом.
        """

        request = GetFileRequest(id=str(file_id))
        response = self.get_file_api(request)

        return response

    def delete_file_api(self, request: DeleteFileRequest) -> Empty:
        """Вызывает RPC удаления файла с готовым запросом.

        Args:
            request: Protobuf-запрос на удаление файла.

        Returns:
            Пустой ответ сервиса после удаления файла.
        """

        return self.call(self.stub.DeleteFile, request)

    def delete_file(self, file_id: UUID) -> Empty:
        """Удаляет файл по его идентификатору.

        Args:
            file_id: Идентификатор удаляемого файла.

        Returns:
            Пустой ответ сервиса после удаления файла.
        """

        request = DeleteFileRequest(id=str(file_id))
        response = self.delete_file_api(request)

        return response
