import grpc
from faker import Faker
from v1.authentication_pb2 import LoginRequest
from v1.authentication_pb2_grpc import AuthenticationServiceStub
from v1.courses_pb2 import GetCourseRequest
from v1.courses_pb2_grpc import CoursesServiceStub
from v1.users_pb2 import CreateUserRequest
from v1.users_pb2_grpc import UsersServiceStub

fake = Faker()

email = fake.unique.email()
password = "123456qQ!"

channel = grpc.insecure_channel("localhost:9000")


users_stub = UsersServiceStub(channel)

create_user_request = CreateUserRequest(
    email=email,
    password=password,
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.first_name(),
)

users_stub.CreateUser(create_user_request)

authentication_stub = AuthenticationServiceStub(channel)

login_request = LoginRequest(email=email, password=password)
login_response = authentication_stub.Login(login_request)

metadata = (
    (
        "authorization",
        f"{login_response.token.token_type} {login_response.token.access_token}",
    ),
)

courses_stub = CoursesServiceStub(channel)

get_course_request = GetCourseRequest(id=fake.uuid4())

try:
    get_course_response = courses_stub.GetCourse(
        request=get_course_request, metadata=metadata
    )
    print(get_course_response)

except grpc.RpcError as e:
    print("Error", e.code(), e.details())
