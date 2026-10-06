from faker import Faker

class Fake:
    def __init__(self, faker: Faker):

        self.faker = faker

    def email(self) -> str:
        return self.faker.email()

    def password(self) -> str:
        return self.faker.password()

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

fake = Fake(faker=Faker())