from django import test

from example import caller
from example import models


class ExampleTestCase(test.TestCase):
    def setUp(self) -> None:
        example = models.Example(enum=models.Example.Enum.EXAMPLE)
        example.save()
        self.example = example

    def test_example(self) -> None:
        self.example.enum = "invalid"

        caller_ = caller.Caller()
        result = caller_.call()
        self.assertTrue(result)
