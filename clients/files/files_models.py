"""Модели данных файла для тестовых фикстур."""

from pydantic import BaseModel, ConfigDict
from v1.files_pb2 import CreateFileRequest, GetFileResponse


class FileFixture(BaseModel):
    """Хранит запрос на создание файла и ответ сервиса."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: CreateFileRequest
    response: GetFileResponse

    @property
    def file_id(self) -> str:
        """Возвращает идентификатор созданного файла.

        Returns:
            Идентификатор файла из ответа сервиса.
        """
        return self.response.file.id
