from dataclasses import dataclass
from typing import Any

from yatl.domains.http import HttpTestStep


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
    steps: list[HttpTestStep]
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
