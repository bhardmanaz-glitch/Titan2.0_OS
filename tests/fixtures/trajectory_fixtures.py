import pytest


@pytest.fixture
def linear_traj(linear_planner):

    return linear_planner.generate(
        start=0,
        end=1,
        duration=2,
    )


@pytest.fixture
def trapezoidal_traj(trapezoidal_planner):

    return trapezoidal_planner.generate(
        start=0,
        end=1,
    )


@pytest.fixture
def reverse_traj(trapezoidal_planner):

    return trapezoidal_planner.generate(
        start=1,
        end=0,
    )


@pytest.fixture
def triangular_traj(trapezoidal_planner):

    return trapezoidal_planner.generate(
        start=0,
        end=0.05,
    )