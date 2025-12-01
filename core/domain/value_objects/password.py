import dataclasses
import re


@dataclasses.dataclass(frozen=True)
class Password:
    value: str

    def __post_init__(self):
        if self.validate(self.value):
            return

    @staticmethod
    def validate(password: str):
        upper_case_regex = re.compile(r"[A-Z]")
        number_regex = re.compile(r"[0-9]")
        special_case_regex = re.compile(r"[!@#$%^&*(),.?\":{}|<>]")

        if len(password) < 8:
            raise ValueError("Password must contain at least 8 characters")

        elif not bool(upper_case_regex.search(password)):
            raise ValueError("Password must contain at least one uppercase letter")

        elif not bool(number_regex.search(password)):
            raise ValueError("Password must contain at least a number")

        elif not bool(special_case_regex.search(password)):
            raise ValueError("Password must contain at least a special case")
