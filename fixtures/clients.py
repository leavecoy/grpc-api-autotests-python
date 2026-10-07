import pytest
from grpc import Channel, insecure_channel

from clients import UsersClient
from clients.authentication.authentication_client import AuthenticationClient
from clients.courses.courses_client import CoursesClient


@pytest.fixture
def grpc_channel():
    channel = insecure_channel("localhost:9000")

    yield channel

    channel.close()


@pytest.fixture
def courses_client(grpc_channel: Channel):
    return CoursesClient(channel=grpc_channel)


@pytest.fixture
def users_client(grpc_channel: Channel):
    return UsersClient(channel=grpc_channel)


@pytest.fixture
def authentication_client(grpc_channel: Channel):
    return AuthenticationClient(channel=grpc_channel)
