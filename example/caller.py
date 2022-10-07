from example import models


class Caller:
    def __init__(self) -> None:
        self.example = models.Example.objects.first()

    def call(self) -> bool:
        if self.example.enum != models.Example.Enum.EXAMPLE:
            return False
        return True
