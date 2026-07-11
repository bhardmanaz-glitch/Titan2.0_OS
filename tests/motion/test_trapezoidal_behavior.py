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

def test_profile_starts_at_zero(behavior):

    progress = behavior._evaluate_profile(
        time=0.0,
        duration=2.0,
    )

    assert progress == 0.0


def test_profile_ends_at_one(behavior):

    progress = behavior._evaluate_profile(
        time=2.0,
        duration=2.0,
    )

    assert progress == 1.0


def test_profile_midpoint(behavior):

    progress = behavior._evaluate_profile(
        time=1.0,
        duration=2.0,
    )

    assert progress == 0.5


def test_profile_quarter_point(behavior):

    progress = behavior._evaluate_profile(
        time=0.5,
        duration=2.0,
    )

    assert progress == 0.25


def test_profile_three_quarter_point(behavior):

    progress = behavior._evaluate_profile(
        time=1.5,
        duration=2.0,
    )

    assert progress == 0.75


def test_profile_returns_normalized_value(behavior):

    progress = behavior._evaluate_profile(
        time=0.73,
        duration=2.0,
    )

    assert 0.0 <= progress <= 1.0

def test_interpolate_returns_start_pose(behavior):

    start = FootPose(0.2, -0.1)
    end = FootPose(0.8, -0.5)

    pose = behavior._interpolate_pose(
        start,
        end,
        progress=0.0,
    )

    assert pose == start


def test_interpolate_returns_end_pose(behavior):

    start = FootPose(0.2, -0.1)
    end = FootPose(0.8, -0.5)

    pose = behavior._interpolate_pose(
        start,
        end,
        progress=1.0,
    )

    assert pose == end


def test_interpolate_midpoint(behavior):

    start = FootPose(0.0, 0.0)
    end = FootPose(2.0, 4.0)

    pose = behavior._interpolate_pose(
        start,
        end,
        progress=0.5,
    )

    assert pose == FootPose(
        1.0,
        2.0,
    )


def test_interpolate_quarter_point(behavior):

    start = FootPose(0.0, 0.0)
    end = FootPose(4.0, 8.0)

    pose = behavior._interpolate_pose(
        start,
        end,
        progress=0.25,
    )

    assert pose == FootPose(
        1.0,
        2.0,
    )


def test_interpolate_preserves_type(behavior):

    pose = behavior._interpolate_pose(
        FootPose(0.0, 0.0),
        FootPose(1.0, 1.0),
        progress=0.5,
    )

    assert isinstance(pose, FootPose)