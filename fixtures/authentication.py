import pytest
from pydantic import BaseModel

from clients.authentication.authentication_client import AuthenticationClient
from clients.types import GRPCMetadata
from fixtures.users import UserFixture


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


@pytest.fixture
def auth_metadata(
    function_user: UserFixture, authentication_client: AuthenticationClient
) -> AuthMetadata:

    response = authentication_client.login(
        email=function_user.request.email, password=function_user.request.password
    )
    metadata = AuthMetadata(
        token=Token(
            token_type=response.token.token_type,
            access_token=response.token.access_token,
            refresh_token=response.token.refresh_token,
        )
    )

    return metadata
