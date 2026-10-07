"""Базовый клиент для тестирования gRPC-сервисов."""

from grpc import Channel

from clients.types import GRPCMetadata


class GRPCTestClient:
    """Хранит gRPC-канал для обращения к сервисам в тестах."""

    def __init__(self, channel: Channel, metadata: GRPCMetadata | None = None):
        """Инициализирует клиент с переданным gRPC-каналом.

        Args:
            channel: Канал для выполнения gRPC-запросов.
        """
        self.channel = channel
        self.metadata = metadata

    def call(self, rpc, request):
        return rpc(request, metadata=self.metadata)
