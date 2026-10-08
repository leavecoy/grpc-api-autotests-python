from pydantic import BaseModel, ConfigDict
from v1.users_pb2 import CreateUserRequest, GetUserResponse


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
