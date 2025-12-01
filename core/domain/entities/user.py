import dataclasses

from core.domain.value_objects import Email, Password, Username


@dataclasses.dataclass
class User:
    id: str
    username: Username
    email: Email
    password: Password
