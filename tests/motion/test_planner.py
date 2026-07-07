import pytest

from titan.motion.planner import TrajectoryPlanner
from titan.motion.profiles import (
    LinearProfile,
    TrapezoidalProfile,
)


# ------------------------------------------------------------
# Construction
# ------------------------------------------------------------

def test_default_profile_is_linear():

    planner = TrajectoryPlanner()

    assert isinstance(
        planner.motion_profile,
        LinearProfile,
    )


def test_custom_profile():

    planner = TrajectoryPlanner(
        profile=TrapezoidalProfile(),
    )

    assert isinstance(
        planner.motion_profile,
        TrapezoidalProfile,
    )


def test_string_profiles_rejected():

    with pytest.raises(TypeError):

        TrajectoryPlanner(
            profile="linear",
        )


# ------------------------------------------------------------
# Profile Switching
# ------------------------------------------------------------

def test_set_profile():

    planner = TrajectoryPlanner()

    planner.set_profile(
        TrapezoidalProfile()
    )

    assert isinstance(
        planner.motion_profile,
        TrapezoidalProfile,
    )


def test_set_profile_rejects_strings():

    planner = TrajectoryPlanner()

    with pytest.raises(TypeError):

        planner.set_profile(
            "linear"
        )


# ------------------------------------------------------------
# Motion Planning
# ------------------------------------------------------------

def test_plan_returns_motion_plan(linear_planner):

    plan = linear_planner.plan(
        start=0,
        end=1,
    )

    assert plan.distance == pytest.approx(1.0)


def test_reverse_plan(linear_planner):

    plan = linear_planner.plan(
        start=1,
        end=0,
    )

    assert plan.direction == -1
    assert plan.distance == pytest.approx(1.0)


def test_zero_distance(linear_planner):

    plan = linear_planner.plan(
        start=1,
        end=1,
    )

    assert plan.distance == 0


# ------------------------------------------------------------
# Trapezoidal Planning
# ------------------------------------------------------------

def test_long_move_has_cruise(linear_planner):

    plan = linear_planner.plan(
        start=0,
        end=1,
    )

    assert plan.cruise_time > 0


def test_short_move_is_triangular(linear_planner):

    plan = linear_planner.plan(
        start=0,
        end=0.05,
    )

    assert plan.cruise_time == pytest.approx(0.0)


# ------------------------------------------------------------
# Limits
# ------------------------------------------------------------

def test_velocity_limit(linear_planner):

    plan = linear_planner.plan(
        start=0,
        end=1,
    )

    assert (
        plan.max_velocity
        <= linear_planner.max_velocity
        + 1e-6
    )


def test_acceleration_limit(linear_planner):

    plan = linear_planner.plan(
        start=0,
        end=1,
    )

    assert (
        plan.max_acceleration
        == linear_planner.max_acceleration
    )


# ------------------------------------------------------------
# Sampling
# ------------------------------------------------------------

def test_dt_preserved(linear_planner):

    plan = linear_planner.plan(
        start=0,
        end=1,
        dt=0.01,
    )

    assert plan.dt == pytest.approx(0.01)


def test_step_count_positive(linear_planner):

    plan = linear_planner.plan(
        start=0,
        end=1,
    )

    assert plan.steps > 0