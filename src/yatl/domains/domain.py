from dataclasses import dataclass
from typing import Any

from yatl.domains.http import ExpectSpec, ExtractSpec, HttpRequest


@dataclass
class TestStep:
    """
    Step specification.

    Attributes:
        name: The name of the step.
        description: The description of the step.
        request: The request specification.
        expect: The expectation specification.
        extract: The extraction specification.
        parametrize: The parametrization specification.
        skip: Whether the step should be skipped.
    """

    name: str | None
    description: str | None
    request: HttpRequest | None
    expect: ExpectSpec | None
    extract: ExtractSpec | None
    parametrize: list[dict] | None
    skip: bool


@dataclass
class TestSpecification:
    """
    Test specification.

    Attributes:
        name: The name of the test.
        base_url: The base URL for the test.
        description: The description of the test.
        steps: The steps of the test.
        skip: Whether the test should be skipped.
    """

    name: str | None
    base_url: str
    description: str | None
    steps: list[TestStep]
    skip: bool


@dataclass
class Context:
    """
    Context for a test run.

    Attributes:
        variables: The variables for the test run.
        extracted: The extracted variables for the test run.
    """

    variables: dict[str, Any]
    extracted: dict[str, Any]
