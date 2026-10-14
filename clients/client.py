"""Базовый клиент для тестирования gRPC-сервисов."""

from grpc import Channel

from clients.types import GRPCMetadata


class GRPCTestClient:
    """Выполняет вызовы gRPC-сервисов с каналом и метаданными клиента."""

    def __init__(self, channel: Channel, metadata: GRPCMetadata | None = None):
        """Инициализирует клиент с переданными gRPC-каналом и метаданными.

        Args:
            channel: Канал для выполнения gRPC-запросов.
            metadata: Метаданные для выполнения gRPC-запросов или None,
                если дополнительные метаданные не нужны.
        """
        self.channel = channel
        self.metadata = metadata

    def call(self, rpc, request):
        """Вызывает RPC с метаданными клиента.

        Args:
            rpc: Метод gRPC-сервиса для вызова.
            request: Protobuf-запрос для передачи сервису.

        Returns:
            Ответ вызываемого метода сервиса.
        """
        return rpc(request, metadata=self.metadata)
