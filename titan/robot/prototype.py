"""
Titan Prototype Configuration
"""

from ..hardware.actuator import Actuator
from .hardware import (
    FEMUR,
    GL30,
    GL40,
    HIP_GEARBOX,
    KNEE_GEARBOX,
    TIBIA,
)
from ..hardware.foot import Foot
from .joint import Joint
from ..hardware.leg import Leg

HIP = Joint(
    name="Hip",
    actuator=Actuator(
        motor=GL40,
        gearbox=HIP_GEARBOX,
    ),
    min_angle=-3.14,
    max_angle=3.14,
)

KNEE = Joint(
    name="Knee",
    actuator=Actuator(
        motor=GL30,
        gearbox=KNEE_GEARBOX,
    ),
    min_angle=-3.14,
    max_angle=0.0,
)

PROTOTYPE_LEG = Leg(
    hip=HIP,
    femur=FEMUR,
    knee=KNEE,
    tibia=TIBIA,
    foot=Foot(),
)

