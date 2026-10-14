"""Фикстуры для создания тестовых файлов и их удаления после тестов."""

from typing import Any, Generator

import pytest
from v1.files_pb2 import DeleteFileRequest

from clients.files.files_client import FilesClient
from clients.files.files_models import FileFixture
from tools.factories.files import files_factory


@pytest.fixture
def function_file(files_client: FilesClient) -> Generator[FileFixture, Any, None]:
    """Создаёт файл с тестовым содержимым и случайным именем для теста.

    После завершения теста удаляет созданный файл.

    Args:
        files_client: Клиент сервиса файлов с метаданными аутентификации.

    Yields:
        Данные запроса на создание файла и ответ сервиса.
    """
    create_request = files_factory.create_file_request()
    create_response = files_client.create_file_api(create_request)

    yield FileFixture(request=create_request, response=create_response)

    delete_request = DeleteFileRequest(id=create_response.file.id)
    files_client.delete_file_api(request=delete_request)
