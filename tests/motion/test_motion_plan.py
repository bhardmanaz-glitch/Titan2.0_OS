import pytest


# ------------------------------------------------------------
# Basic Fields
# ------------------------------------------------------------

def test_start_position(trapezoidal_plan):
    assert trapezoidal_plan.start == pytest.approx(0.0)


def test_end_position(trapezoidal_plan):
    assert trapezoidal_plan.end == pytest.approx(1.0)


def test_distance(trapezoidal_plan):
    assert trapezoidal_plan.distance == pytest.approx(1.0)


def test_direction(trapezoidal_plan):
    assert trapezoidal_plan.direction == 1


# ------------------------------------------------------------
# Timing
# ------------------------------------------------------------

def test_duration_positive(trapezoidal_plan):
    assert trapezoidal_plan.duration > 0


def test_accel_time_positive(trapezoidal_plan):
    assert trapezoidal_plan.accel_time > 0


def test_decel_time_positive(trapezoidal_plan):
    assert trapezoidal_plan.decel_time > 0


def test_total_time_matches_segments(trapezoidal_plan):

    total = (
        trapezoidal_plan.accel_time
        + trapezoidal_plan.cruise_time
        + trapezoidal_plan.decel_time
    )

    assert total == pytest.approx(
        trapezoidal_plan.duration
    )


# ------------------------------------------------------------
# Distances
# ------------------------------------------------------------

def test_distance_segments_sum(trapezoidal_plan):

    total = (
        trapezoidal_plan.accel_distance
        + trapezoidal_plan.cruise_distance
        + trapezoidal_plan.decel_distance
    )

    assert total == pytest.approx(
        trapezoidal_plan.distance
    )


# ------------------------------------------------------------
# Limits
# ------------------------------------------------------------

def test_velocity_positive(trapezoidal_plan):
    assert trapezoidal_plan.max_velocity > 0


def test_acceleration_positive(trapezoidal_plan):
    assert trapezoidal_plan.max_acceleration > 0


# ------------------------------------------------------------
# Sampling
# ------------------------------------------------------------

def test_steps_positive(trapezoidal_plan):
    assert trapezoidal_plan.steps > 0


def test_dt_positive(trapezoidal_plan):
    assert trapezoidal_plan.dt > 0


# ------------------------------------------------------------
# Reverse Motion
# ------------------------------------------------------------

def test_reverse_direction(reverse_plan):
    assert reverse_plan.direction == -1


def test_reverse_distance_positive(reverse_plan):
    assert reverse_plan.distance > 0


def test_reverse_duration_positive(reverse_plan):
    assert reverse_plan.duration > 0


# ------------------------------------------------------------
# Triangular Profile
# ------------------------------------------------------------

def test_triangular_has_zero_cruise(triangular_plan):
    assert triangular_plan.cruise_time == pytest.approx(0.0)


def test_triangular_distance(triangular_plan):
    assert triangular_plan.cruise_distance == pytest.approx(0.0)


# ------------------------------------------------------------
# Trapezoidal Profile
# ------------------------------------------------------------

def test_trapezoidal_has_cruise(trapezoidal_plan):
    assert trapezoidal_plan.cruise_time > 0


def test_trapezoidal_distance(trapezoidal_plan):
    assert trapezoidal_plan.cruise_distance > 0