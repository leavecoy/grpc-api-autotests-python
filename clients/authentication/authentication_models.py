"""Модели токенов и метаданных аутентификации."""

from pydantic import BaseModel

from clients.types import GRPCMetadata


class Token(BaseModel):
    """Хранит тип токена, токен доступа и токен обновления."""

    token_type: str
    access_token: str
    refresh_token: str


class AuthMetadata(BaseModel):
    """Формирует метаданные аутентификации из токена."""

    token: Token

    @property
    def metadata(self) -> GRPCMetadata:
        """Возвращает метаданные для аутентификации gRPC-запросов.

        Returns:
            Метаданные с типом токена и токеном доступа.
        """
        return (
            (
                "authorization",
                f"{self.token.token_type} {self.token.access_token}",
            ),
        )
