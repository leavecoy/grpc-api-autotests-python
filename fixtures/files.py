"""Фикстуры для создания тестовых файлов."""

import pytest
from tools.factories.files import files_factory

from clients.files.files_client import FilesClient
from clients.files.files_models import FileFixture


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    """Создаёт файл с тестовым содержимым и случайным именем для теста.

    Args:
        files_client: Клиент сервиса файлов с метаданными аутентификации.

    Returns:
        Данные запроса на создание файла и ответ сервиса.
    """
    request = files_factory.create_file_request()
    response = files_client.create_file_api(request)

    return FileFixture(request=request, response=response)
