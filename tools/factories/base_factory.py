"""Базовая фабрика запросов с генерацией тестовых данных."""

from typing import Any, Callable

from tools.fakers import Fake


class BaseFactory:
    """Предоставляет генератор данных и подстановку значений по умолчанию."""

    def __init__(self, fake_generator: Fake):
        """Инициализирует базовую фабрику запросов.

        Args:
            fake_generator: Генератор случайных тестовых данных.
        """
        self.fake = fake_generator

    @staticmethod
    def _resolve(value: Any | None, default_factory: Callable[[], Any]) -> Any:
        """Подставляет сгенерированное значение, если передано None.

        Args:
            value: Заданное значение или None.
            default_factory: Функция генерации значения по умолчанию.

        Returns:
            Переданное значение или результат вызова генератора.
        """
        return default_factory() if value is None else value
