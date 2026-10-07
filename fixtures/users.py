import pytest
from pydantic import BaseModel, ConfigDict
from v1.users_pb2 import CreateUserRequest, GetUserResponse

from clients.users.users_client import UsersClient
from tools.factories.users import user_factory


class UserFixture(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: CreateUserRequest
    response: GetUserResponse

    @property
    def email(self) -> str:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def user_id(self) -> str:
        return self.response.user.id


@pytest.fixture
def function_user(users_client: UsersClient) -> UserFixture:
    request = user_factory.create_user_request()
    response = users_client.create_user_api(request)

    return UserFixture(request=request, response=response)
