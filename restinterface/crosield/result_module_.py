"""
Result Module

2025.5.7

This module provides a type-safe Result type inspired by Rust's Result.
It supports Ok and Err types, with methods for easy value handling,
error propagation, and functional-style chaining.

Classes:
- Ok: Represents a successful result.
- Err: Represents an error result.

Usage:
    from result_module import Ok, Err, Result

    result1: Result[int, str] = Ok(42)
    result2: Result[int, str] = Err("An error occurred")

    print(result1.unwrap())  # 42
    print(result2.unwrap_err())  # "An error occurred"

"""

from typing import Generic, TypeVar, Callable, Union

T = TypeVar('T')
E = TypeVar('E')
U = TypeVar('U')
F = TypeVar('F')

class Ok(Generic[T, E]):
    def __init__(self, value: T):
        self.value = value

    def unwrap(self) -> T:
        return self.value

    def unwrap_err(self) -> E:
        raise ValueError("Cannot unwrap_err on Ok value.")

    def expect(self, message: str) -> T:
        return self.value

    def expect_err(self, message: str) -> E:
        raise ValueError(message)

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False

    def match(self, on_ok: Callable[[T], U], on_err: Callable[[E], U]) -> U:
        return on_ok(self.value)

    def map(self, func: Callable[[T], U]) -> 'Ok[U, E]':
        return Ok(func(self.value))

    def map_err(self, func: Callable[[E], F]) -> 'Ok[T, F]':
        return self

    def and_then(self, func: Callable[[T], 'Result[U, E]']) -> 'Result[U, E]':
        return func(self.value)

    def __repr__(self) -> str:
        return f"Ok({self.value})"


class Err(Generic[T, E]):
    def __init__(self, error: E):
        self.error = error

    def unwrap(self) -> T:
        raise ValueError(f"Cannot unwrap on Err value: {self.error}")

    def unwrap_err(self) -> E:
        return self.error

    def expect(self, message: str) -> T:
        raise ValueError(message)

    def expect_err(self, message: str) -> E:
        return self.error

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True

    def match(self, on_ok: Callable[[T], U], on_err: Callable[[E], U]) -> U:
        return on_err(self.error)

    def map(self, func: Callable[[T], U]) -> 'Err[U, E]':
        return self

    def map_err(self, func: Callable[[E], F]) -> 'Err[T, F]':
        return Err(func(self.error))

    def and_then(self, func: Callable[[T], 'Result[U, E]']) -> 'Err[T, E]':
        return self

    def __repr__(self) -> str:
        return f"Err({self.error})"


Result = Union[Ok[T, E], Err[T, E]]
