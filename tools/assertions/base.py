from typing import Any, Sized

import grpc
from v1.common_pb2 import Empty


def assert_equal(actual: Any, expected: Any, name: str):

    assert actual == expected, (
        f"Некорректное значение {name}."
        f"Ожидаемое значение: {expected};"
        f"Фактическое значение: {actual}."
    )


def assert_length(actual: Sized, expected_length: int, name: str):

    assert len(actual) == expected_length, (
        f"Некорректная длина {name}."
        f"Ожидаемая длина: {expected_length};"
        f"Фактическая длина: {len(actual)}"
    )


def assert_is_empty(actual: Any, name: str):
    assert actual is Empty, f"Некорректное значение f{name}. Ожидался Empty-объект."


def assert_not_empty(actual: Any, name: str):

    assert actual, f"Некорректное значение {name}." f"Фактическое значение пусто."


def assert_grpc_status(error: grpc.RpcError, expected: grpc.StatusCode):

    assert error.code() == expected, (
        "Неверный статус-код ошибки."
        f"Ожидаемый статус-код: {expected}"
        f"Фактический статус-код: {error.code()}"
    )
