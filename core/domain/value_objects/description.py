import dataclasses


@dataclasses.dataclass(frozen=True)
class Description:
    value: str

    def __post_init__(self):
        if not self.validate(self.value):
            raise ValueError("Description must contain at least 20 characteres")

    @staticmethod
    def validate(description: str) -> bool:
        return len(description) > 20
