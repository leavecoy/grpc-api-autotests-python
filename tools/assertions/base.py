"""Базовые проверки значений, длины, пустых ответов и статусов gRPC."""

from typing import Any, Sized

import grpc
from v1.common_pb2 import Empty


def assert_equal(actual: Any, expected: Any, name: str):
    """Проверяет равенство фактического и ожидаемого значений.

    Args:
        actual: Фактическое значение.
        expected: Ожидаемое значение.
        name: Название проверяемого значения для сообщения об ошибке.

    Raises:
        AssertionError: Если значения не равны.
    """

    assert actual == expected, (
        f"Некорректное значение {name}."
        f"Ожидаемое значение: {expected};"
        f"Фактическое значение: {actual}."
    )


def assert_length(actual: Sized, expected_length: int, name: str):
    """Проверяет длину объекта.

    Args:
        actual: Объект, поддерживающий получение длины через len().
        expected_length: Ожидаемая длина объекта.
        name: Название проверяемого объекта для сообщения об ошибке.

    Raises:
        AssertionError: Если длина объекта отличается от ожидаемой.
    """

    assert len(actual) == expected_length, (
        f"Некорректная длина {name}."
        f"Ожидаемая длина: {expected_length};"
        f"Фактическая длина: {len(actual)}"
    )


def assert_is_empty(actual: Any, name: str):
    """Проверяет, что объект является экземпляром protobuf-сообщения Empty.

    Args:
        actual: Проверяемый объект.
        name: Название проверяемого объекта для сообщения об ошибке.

    Raises:
        AssertionError: Если объект не является экземпляром Empty.
    """
    assert isinstance(
        actual, Empty
    ), f"Некорректный тип {name}: ожидается объект класса Empty."


def assert_not_empty(actual: Any, name: str):
    """Проверяет, что значение истинно при приведении к bool.

    Args:
        actual: Проверяемое значение.
        name: Название проверяемого значения для сообщения об ошибке.

    Raises:
        AssertionError: Если значение ложно, например None, 0 или пустая строка.
    """

    assert actual, f"Некорректное значение {name}." f"Фактическое значение пусто."


def assert_grpc_status(error: grpc.RpcError, expected: grpc.StatusCode):
    """Проверяет статус-код ошибки gRPC.

    Args:
        error: Ошибка, полученная при выполнении gRPC-запроса.
        expected: Ожидаемый статус-код ошибки.

    Raises:
        AssertionError: Если статус-код ошибки отличается от ожидаемого.
    """

    assert error.code() == expected, (
        "Неверный статус-код ошибки."
        f"Ожидаемый статус-код: {expected}"
        f"Фактический статус-код: {error.code()}"
    )
