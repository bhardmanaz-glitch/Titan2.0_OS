import pytest

from titan.motion.behaviors.trapezoidal_behavior import TrapezoidalBehavior
from titan.motion.foot_pose import FootPose

@pytest.fixture
def behavior() -> TrapezoidalBehavior:
    return TrapezoidalBehavior()

def test_create_behavior(behavior):
    assert isinstance(behavior, TrapezoidalBehavior)

def test_generate_rejects_negative_duration(behavior):
 
    start = FootPose(0.0, 0.0)
    end = FootPose(1.0, 0.0)

    with pytest.raises(ValueError):
        behavior.generate(
            start,
            end,
            duration=-1.0,
            dt=0.1,
        )

def test_generate_rejects_zero_dt(behavior):

    start = FootPose(0.0, 0.0)
    end = FootPose(1.0, 0.0)

    with pytest.raises(ValueError):
        behavior.generate(
            start,
            end,
            duration=1.0,
            dt=0.0,
        )

def test_generate_rejects_negative_dt(behavior):

    start = FootPose(0.0, 0.0)
    end = FootPose(1.0, 0.0)

    with pytest.raises(ValueError):
        behavior.generate(
            start,
            end,
            duration=1.0,
            dt=-0.1,
        )

def test_generate_accepts_zero_duration_for_identical_poses(behavior):

    pose = FootPose(0.0, 0.0)

    behavior.generate(
        pose,
        pose,
        duration=0.0,
        dt=0.1,
    )
def test_generate_rejects_zero_duration_motion(behavior):

    start = FootPose(0.0, 0.0)
    end = FootPose(1.0, 0.0)

    with pytest.raises(ValueError):
        behavior.generate(
            start,
            end,
            duration=0.0,
            dt=0.1,
        )

@pytest.fixture
def behavior() -> TrapezoidalBehavior:
    return TrapezoidalBehavior()

def test_generate_sample_times_includes_endpoints(behavior):

    times = behavior._generate_sample_times(
        duration=1.0,
        dt=0.25,
    )

    assert times == pytest.approx(
        (
            0.0,
            0.25,
            0.50,
            0.75,
            1.0,
        )
    )

def test_generate_sample_times_handles_uneven_dt(behavior):

    times = behavior._generate_sample_times(
        duration=1.0,
        dt=0.30,
    )

    assert times == pytest.approx(
        (
            0.0,
            0.3,
            0.6,
            0.9,
            1.0,
        )
    )

def test_generate_sample_times_handles_large_dt(behavior):

    times = behavior._generate_sample_times(
        duration=0.2,
        dt=1.0,
    )

    assert times == pytest.approx(
        (
            0.0,
            0.2,
        )    
    )

def test_generate_sample_times_never_duplicates_endpoint(behavior):

    times = behavior._generate_sample_times(
        duration=1.0,
        dt=0.5,
    )

    assert times.count(1.0) == 1

def test_generate_sample_times_is_monotonic(behavior):

    times = behavior._generate_sample_times(
        duration=1.0,
        dt=0.17,
    )

    assert all(
        earlier < later
        for earlier, later in zip(times, times[1:])
    )

def test_generate_sample_times_starts_at_zero(behavior):

    times = behavior._generate_sample_times(
        duration=1.0,
        dt=0.25,
    )

    assert times[0] == 0.0
