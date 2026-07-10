import pytest

from titan.motion.behaviors.trapezoidal_behavior import TrapezoidalBehavior


def test_create_behavior():

    behavior = TrapezoidalBehavior()

    assert isinstance(behavior, TrapezoidalBehavior)


def test_generate_not_implemented():

    behavior = TrapezoidalBehavior()

    with pytest.raises(NotImplementedError):
        behavior.generate(0.0, 10.0)