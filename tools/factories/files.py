"""Фабрика запросов на создание файлов."""

from pathlib import Path

from v1.files_pb2 import CreateFileRequest

from tools.factories.base_factory import BaseFactory
from tools.fakers import Fake, fake


class FilesFactory(BaseFactory):
    """Формирует запросы на создание файлов с тестовыми данными."""

    def __init__(self, fake_generator: Fake):
        """Инициализирует фабрику запросов.

        Args:
            fake_generator: Генератор случайных данных для файлов.
        """
        super().__init__(fake_generator)
        self.fake = fake_generator

    def create_file_request(
        self,
        filename: str | None = None,
        directory: str | None = None,
        testfile_path: Path | None = None,
    ) -> CreateFileRequest:
        """Формирует запрос на создание файла с содержимым локального файла.

        Args:
            filename: Имя файла или None для генерации.
            directory: Директория для сохранения файла или None для testdata.
            testfile_path: Путь к локальному файлу или None для использования
                tools/testdata/test_image.png.

        Returns:
            Protobuf-запрос на создание файла.
        """

        file_path = (
            testfile_path
            if testfile_path is not None
            else Path("tools/testdata/test_image.png")
        )
        directory_path = directory if directory is not None else "testdata"

        request = CreateFileRequest(
            filename=self._resolve(filename, self.fake.filename),
            directory=directory_path,
            content=file_path.read_bytes(),
        )

        return request


files_factory = FilesFactory(fake_generator=fake)
