import pytest
from grpc import Channel, insecure_channel

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_models import AuthMetadata
from clients.courses.courses_client import CoursesClient
from clients.exercises.exercises_client import ExercisesClient
from clients.files.files_client import FilesClient
from clients.users.users_client import UsersClient


@pytest.fixture
def grpc_channel():
    channel = insecure_channel("localhost:9000")

    yield channel

    channel.close()


@pytest.fixture
def courses_client(grpc_channel: Channel, auth_metadata: AuthMetadata):
    return CoursesClient(channel=grpc_channel, metadata=auth_metadata.metadata)


@pytest.fixture
def public_users_client(grpc_channel: Channel):
    return UsersClient(channel=grpc_channel)


@pytest.fixture
def private_users_client(grpc_channel: Channel, auth_metadata: AuthMetadata):
    return UsersClient(channel=grpc_channel, metadata=auth_metadata.metadata)


@pytest.fixture
def files_client(grpc_channel: Channel, auth_metadata: AuthMetadata):
    return FilesClient(channel=grpc_channel, metadata=auth_metadata.metadata)


@pytest.fixture
def exercises_client(grpc_channel: Channel, auth_metadata: AuthMetadata):
    return ExercisesClient(channel=grpc_channel, metadata=auth_metadata.metadata)


@pytest.fixture
def authentication_client(grpc_channel: Channel):
    return AuthenticationClient(channel=grpc_channel)
