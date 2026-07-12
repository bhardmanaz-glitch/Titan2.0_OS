from titan.hardware.commissioned_joint import (
    CommissionedJoint,
)

from titan.hardware.mock_axis import MockAxis

from titan.hardware.actuator_mapper import (
    ActuatorMapper,
)

from titan.hardware.prototype import (
    PROTOTYPE_LEG,
)

def test_create_commissioned_joint():

    joint = PROTOTYPE_LEG.hip

    driver = MockAxis()

    mapper = ActuatorMapper(
        gear_ratio=36,
        sign=1,
        zero_offset=0.0,
    )

    commissioned = CommissionedJoint(
        joint=joint,
        driver=driver,
        mapper=mapper,
    )

    assert commissioned.joint is joint

def test_stores_driver():

    commissioned = CommissionedJoint(
        joint=PROTOTYPE_LEG.hip,
        driver=MockAxis(),
        mapper=ActuatorMapper(
            gear_ratio=36,
            sign=1,
            zero_offset=0.0,
        ),
    )

    assert isinstance(
        commissioned.driver,
        MockAxis,
    )

def test_stores_mapper():

    mapper = ActuatorMapper(
        gear_ratio=36,
        sign=1,
        zero_offset=0.0,
    )

    commissioned = CommissionedJoint(
        joint=PROTOTYPE_LEG.hip,
        driver=MockAxis(),
        mapper=mapper,
    )

    assert commissioned.mapper is mapper