from uuid import UUID

from grpc import Channel
from v1.common_pb2 import Empty
from v1.users_pb2 import (
    CreateUserRequest,
    GetUserRequest,
    GetUserResponse,
    UpdateUserRequest,
)
from v1.users_pb2_grpc import UsersServiceStub

from tests.clients.client import GRPCTestClient


class UsersGRPCTestClient(GRPCTestClient):

    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = UsersServiceStub(self.channel)

    def create_user_api(self, request: CreateUserRequest) -> GetUserResponse:

        return self.stub.CreateUser(request)

    def create_user(
        self,
        email: str,
        password: str,
        last_name: str,
        first_name: str,
        middle_name: str,
    ) -> GetUserResponse:

        request = CreateUserRequest(
            email=email,
            password=password,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
        )
        response = self.create_user_api(request)

        return response

    def update_user_api(self, request: UpdateUserRequest) -> GetUserResponse:

        return self.stub.UpdateUser(request)

    def update_user(
        self,
        user_id: UUID,
        email: str | None = None,
        last_name: str | None = None,
        first_name: str | None = None,
        middle_name: str | None = None,
    ) -> GetUserResponse:
        request = UpdateUserRequest(
            id=str(user_id),
            email=email,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
        )
        response = self.update_user_api(request)

        return response

    def get_user_api(self, request: GetUserRequest) -> GetUserResponse:

        return self.stub.GetUser(request)

    def get_user(self, user_id: UUID) -> GetUserResponse:

        request = GetUserRequest(id=str(user_id))
        response = self.get_user_api(request)

        return response

    def get_me_api(self, request: Empty) -> GetUserResponse:

        return self.stub.GetMe(request)

    def get_me(self) -> GetUserResponse:

        request = Empty()
        response = self.get_me_api(request)
        return response

    def delete_user_api(self, request: GetUserRequest) -> Empty:

        return self.stub.DeleteUser(request)

    def delete_user(self, user_id: UUID) -> Empty:

        request = GetUserRequest(id=str(user_id))
        response = self.delete_user_api(request)

        return response
