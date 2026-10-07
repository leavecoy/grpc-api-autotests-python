from clients.courses.courses_client import CoursesClient
from fixtures.authentication import AuthMetadata
from fixtures.users import UserFixture


def test_function_user(function_user: UserFixture):
    print(function_user)


def test_authorized_user(auth_metadata: AuthMetadata):
    print(auth_metadata.metadata)


def test_courses_client(courses_client: CoursesClient):
    courses_client.create_course(
        title="title",
        description="desc",
        preview_file_id="7f6e0b47-0e7c-4f7b-8e44-7c3f1d0d7f2a",
        created_by_user_id="7f6e0b47-0e7c-4f7b-8e44-7c3f1d0d7f2a",
    )
