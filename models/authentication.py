from pydantic import BaseModel

from clients.types import GRPCMetadata


class Token(BaseModel):
    token_type: str
    access_token: str
    refresh_token: str


class AuthMetadata(BaseModel):
    token: Token

    @property
    def metadata(self) -> GRPCMetadata:
        return (
            (
                "authorization",
                f"{self.token.token_type} {self.token.access_token}",
            ),
        )
