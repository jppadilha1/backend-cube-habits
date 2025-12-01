import dataclasses


@dataclasses.dataclass(frozen=True)
class Username:
    value: str

    def __post_init__(self):
        if not self.validate(self.value):
            raise ValueError("Username must contain at least 5 characteres")

    @staticmethod
    def validate(username: str) -> bool:
        return len(username) > 5
