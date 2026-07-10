import pytest

from titan.motion.behaviors.behavior import MotionBehavior


def test_motion_behavior_is_abstract():

    with pytest.raises(TypeError):
        MotionBehavior()