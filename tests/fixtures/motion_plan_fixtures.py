import pytest


@pytest.fixture
def trapezoidal_plan(trapezoidal_planner):

    return trapezoidal_planner.plan(
        start=0,
        end=1,
    )


@pytest.fixture
def triangular_plan(trapezoidal_planner):

    return trapezoidal_planner.plan(
        start=0,
        end=0.05,
    )


@pytest.fixture
def reverse_plan(trapezoidal_planner):

    return trapezoidal_planner.plan(
        start=1,
        end=0,
    )