import pytest

from titan.motion.planner import TrajectoryPlanner
from titan.motion.profiles import TrapezoidalProfile
from titan.motion.trajectory import Trajectory


# ------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------

@pytest.fixture
def planner():
    """
    Standard planner used by the majority of trajectory tests.
    """
    return TrajectoryPlanner(
        profile=TrapezoidalProfile(),
        max_velocity=0.5,
        max_acceleration=1.0,
    )


# ------------------------------------------------------------
# Basic Generation
# ------------------------------------------------------------

def test_generate_returns_motion_points(planner):

    trajectory = planner.generate(
        start=0.0,
        end=1.0,
        dt=0.1,
    )

    assert isinstance(trajectory, Trajectory)
    assert len(trajectory.points) > 0


def test_first_point_matches_start(planner):

    trajectory = planner.generate(
        start=0,
        end=1,
        dt=0.1,
    )

    first = trajectory[0]

    assert first.position == pytest.approx(0.0)
    assert first.velocity == pytest.approx(0.0)
    assert first.time == pytest.approx(0.0)


def test_last_point_matches_end(planner):

    trajectory = planner.generate(
        start=0,
        end=1,
        dt=0.1,
    )

    last = trajectory[-1]

    assert last.position == pytest.approx(1.0)
    assert last.velocity == pytest.approx(0.0)


# ------------------------------------------------------------
# Motion Properties
# ------------------------------------------------------------

def test_time_always_increases(planner):

    trajectory = planner.generate(
        start=0,
        end=1,
        dt=0.1,
    )

    for previous, current in zip(
        trajectory,
        trajectory[1:]
    ):
        assert current.time > previous.time


def test_position_always_increases(planner):

    trajectory = planner.generate(
        start=0,
        end=1,
        dt=0.1,
    )

    for previous, current in zip(
        trajectory,
        trajectory[1:]
    ):
        assert current.position >= previous.position


def test_velocity_never_exceeds_limit(planner):

    trajectory = planner.generate(
        start=0,
        end=1,
        dt=0.05,
    )

    for point in trajectory:
        assert abs(point.velocity) <= planner.max_velocity + 1e-6


def test_acceleration_never_exceeds_limit(planner):

    trajectory = planner.generate(
        start=0,
        end=1,
        dt=0.05,
    )

    for point in trajectory:
        assert abs(point.acceleration) <= planner.max_acceleration + 1e-6


# ------------------------------------------------------------
# Reverse Motion
# ------------------------------------------------------------

def test_reverse_motion(planner):

    trajectory = planner.generate(
        start=1,
        end=0,
        dt=0.1,
    )

    assert trajectory[0].position == pytest.approx(1.0)
    assert trajectory[-1].position == pytest.approx(0.0)

    for previous, current in zip(
        trajectory,
        trajectory[1:]
    ):
        assert current.position <= previous.position


def test_reverse_velocity_negative(planner):

    trajectory = planner.generate(
        start=1,
        end=0,
        dt=0.05,
    )

    velocities = [
        p.velocity
        for p in trajectory[1:-1]
    ]

    assert all(v <= 0 for v in velocities)


# ------------------------------------------------------------
# Profile Shape
# ------------------------------------------------------------

def test_triangular_profile_has_no_cruise(planner):

    trajectory = planner.generate(
        start=0,
        end=0.1,
        dt=0.02,
    )

    max_velocity = max(
        abs(point.velocity)
        for point in trajectory
    )

    assert max_velocity < planner.max_velocity


def test_trapezoidal_profile_has_cruise_phase(planner):

    trajectory = planner.generate(
        start=0,
        end=2,
        dt=0.02,
    )

    cruise_points = [
        point
        for point in trajectory
        if abs(point.velocity - planner.max_velocity)
        < 1e-6
    ]

    assert len(cruise_points) > 3


# ------------------------------------------------------------
# Velocity Behavior
# ------------------------------------------------------------

def test_velocity_increases_during_acceleration(planner):

    trajectory = planner.generate(
        start=0,
        end=1,
        dt=0.02,
    )

    previous = trajectory[0].velocity

    for point in trajectory[1:]:

        if point.acceleration <= 0:
            break

        assert point.velocity >= previous

        previous = point.velocity


def test_velocity_decreases_during_deceleration(planner):

    trajectory = planner.generate(
        start=0,
        end=1,
        dt=0.02,
    )

    started = False
    previous = None

    for point in trajectory:

        if point.acceleration < 0:

            if not started:
                started = True
                previous = point.velocity
                continue

            assert point.velocity <= previous

            previous = point.velocity


# ------------------------------------------------------------
# Resolution Independence
# ------------------------------------------------------------

def test_final_position_independent_of_dt(planner):

    coarse = planner.generate(
        start=0,
        end=1,
        dt=0.1,
    )

    medium = planner.generate(
        start=0,
        end=1,
        dt=0.05,
    )

    fine = planner.generate(
        start=0,
        end=1,
        dt=0.01,
    )

    assert coarse[-1].position == pytest.approx(1.0)
    assert medium[-1].position == pytest.approx(1.0)
    assert fine[-1].position == pytest.approx(1.0)


def test_dt_changes_number_of_points(planner):

    coarse = planner.generate(
        start=0,
        end=1,
        dt=0.1,
    )

    fine = planner.generate(
        start=0,
        end=1,
        dt=0.01,
    )

    assert len(fine) > len(coarse)


# ------------------------------------------------------------
# Overshoot Protection
# ------------------------------------------------------------

def test_position_never_overshoots_goal(planner):

    trajectory = planner.generate(
        start=0,
        end=1,
        dt=0.01,
    )

    for point in trajectory:
        assert point.position <= 1.0 + 1e-6


def test_reverse_motion_never_overshoots_goal(planner):

    trajectory = planner.generate(
        start=1,
        end=0,
        dt=0.01,
    )

    for point in trajectory:
        assert point.position >= -1e-6