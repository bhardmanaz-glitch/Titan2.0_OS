import pytest

from titan.motion.executor import TrajectoryExecutor


@pytest.fixture
def executor(
    commissioned_joint,
):
    """
    TrajectoryExecutor operating on the prototype hip joint.
    """

    return TrajectoryExecutor(
        commissioned_joint,
    )