"""Базовый клиент для тестирования gRPC-сервисов."""

from grpc import Channel


class GRPCTestClient:
    """Хранит gRPC-канал для обращения к сервисам в тестах."""

    def __init__(self, channel: Channel):
        """Инициализирует клиент с переданным gRPC-каналом.

        Args:
            channel: Канал для выполнения gRPC-запросов.
        """
        self.channel = channel
