from typing import Callable

from v1.users_pb2 import CreateUserRequest

from tools.fakers import Fake, fake


class UserFactory:
    def __init__(self, fake_generator: Fake):
        self.fake = fake_generator

    @staticmethod
    def _resolve(value: str | None, default_factory: Callable[[], str]) -> str:
        return default_factory() if value is None else value

    def create_user_request(
        self,
        email: str | None = None,
        password: str | None = None,
        last_name: str | None = None,
        first_name: str | None = None,
        middle_name: str | None = None,
    ) -> CreateUserRequest:

        request = CreateUserRequest(
            email=self._resolve(email, self.fake.email),
            password=self._resolve(password, self.fake.password),
            last_name=self._resolve(last_name, self.fake.last_name),
            first_name=self._resolve(first_name, self.fake.first_name),
            middle_name=self._resolve(middle_name, self.fake.middle_name),
        )

        return request


user_factory = UserFactory(fake_generator=fake)
