import pytest


# ------------------------------------------------------------
# Construction
# ------------------------------------------------------------

def test_generates_correct_number_of_points(linear_planner):

    trajectory = linear_planner.generate(
        start=0,
        end=1,
        duration=2,
        dt=0.1,
    )

    plan = linear_planner.plan(
        start=0,
        end=1,
        duration=2,
        dt=0.1,
    )

    assert len(trajectory) == plan.steps + 1


# ------------------------------------------------------------
# Position
# ------------------------------------------------------------

def test_starts_at_zero(linear_traj):

    assert linear_traj[0].position == pytest.approx(0.0)


def test_ends_at_goal(linear_traj):

    assert linear_traj[-1].position == pytest.approx(1.0)


def test_position_monotonic(linear_traj):

    previous = linear_traj[0].position

    for point in linear_traj[1:]:

        assert point.position >= previous

        previous = point.position


# ------------------------------------------------------------
# Velocity
# ------------------------------------------------------------

def test_velocity_constant(linear_traj):

    expected = linear_traj[0].velocity

    for point in linear_traj:

        assert point.velocity == pytest.approx(expected)


# ------------------------------------------------------------
# Acceleration
# ------------------------------------------------------------

def test_acceleration_zero(linear_traj):

    for point in linear_traj:

        assert point.acceleration == pytest.approx(0.0)


# ------------------------------------------------------------
# Timing
# ------------------------------------------------------------

def test_dt_preserved(linear_traj):

    for point in linear_traj:

        assert point.dt == pytest.approx(0.02)


def test_time_monotonic(linear_traj):

    previous = -1

    for point in linear_traj:

        assert point.time > previous

        previous = point.time


# ------------------------------------------------------------
# Reverse Motion
# ------------------------------------------------------------

def test_reverse_positions_monotonic(reverse_traj):

    previous = reverse_traj[0].position

    for point in reverse_traj[1:]:

        assert point.position <= previous

        previous = point.position


def test_reverse_velocity_negative(reverse_traj):

    for point in reverse_traj:

        assert point.velocity <= 0


def test_reverse_ends_at_zero(reverse_traj):

    assert reverse_traj[-1].position == pytest.approx(0.0)