import pytest

from titan.motion.behaviors import TrapezoidalBehavior
from titan.motion.behaviors import MotionBehavior
from titan.motion.foot_planner import FootPlanner


class FakeBehavior(MotionBehavior):

    def __init__(self):
        self.calls = []
        self.result = object()

    def generate(self, start, end, duration, dt):
        self.calls.append((start, end, duration, dt))
        return self.result


@pytest.fixture
def fake_behavior() -> FakeBehavior:
    return FakeBehavior()

@pytest.fixture
def planner(fake_behavior) -> FootPlanner:
    return FootPlanner(
        behavior=fake_behavior,
    )

def test_create_foot_planner():

    planner = FootPlanner(
        behavior=TrapezoidalBehavior(),
    )

    assert isinstance(planner, FootPlanner)

def test_accepts_motion_behavior():

    behavior = TrapezoidalBehavior()

    planner = FootPlanner(
        behavior=behavior,
    )

    assert planner.behavior is behavior

def test_generate_delegates_to_behavior(
        planner,
        fake_behavior,
    ):
       
    start = object()
    end = object()

    planner.generate(start, end, 2.0, 0.01)

    assert fake_behavior.calls == [
        (start, end, 2.0, 0.01)
]

def test_generate_returns_behavior_result(
        planner, 
        fake_behavior, 
    ):

    start = object()
    end = object()

    result = planner.generate(
        start,
        end,
        2.0,
        0.01,
    )

    assert result is fake_behavior.result

