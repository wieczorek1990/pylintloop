import typing


class StringValueTuple(tuple):
    value: str


def auto(
    code: typing.Any, name: str, type_: typing.Type[typing.Any]
) -> typing.Any:
    return type_([code, name])


def string_auto(code: str, name: str) -> StringValueTuple:
    return auto(code, name, StringValueTuple)
