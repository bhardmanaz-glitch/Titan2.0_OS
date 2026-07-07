from titan.hardware.motor import Motor
from titan.hardware.gearbox import Gearbox
from titan.hardware.actuator import Actuator
from titan.hardware.joint import Joint
from titan.hardware.link import Link
from titan.hardware.foot import Foot
from titan.hardware.leg import Leg

hip_motor = Motor(
    name="Cubemars GL40",
)

hip_gearbox = Gearbox(
    name="Hip Planetary",
    ratio=36.0,
)

hip_actuator = Actuator(
    motor=hip_motor,
    gearbox=hip_gearbox,
)

hip_joint = Joint(
    name="Hip",
    actuator=hip_actuator,
    min_angle=-1.5,
    max_angle=1.5,
)

femur = Link(
    name="Femur",
    length=0.11628,
)

knee_motor = Motor(
    name="Cubemars GL30",
)

knee_gearbox = Gearbox(
    name="Knee Belt Reduction",
    ratio=9.0,
)

knee_actuator = Actuator(
    motor=knee_motor,
    gearbox=knee_gearbox,
)

knee_joint = Joint(
    name="Knee",
    actuator=knee_actuator,
    min_angle=-2.6,
    max_angle=0.0,
)

tibia = Link(
    name="Tibia",
    length=0.15875,
)

foot = Foot()

PROTOTYPE_LEG = Leg(
    name="Prototype",

    hip=hip_joint,
    knee=knee_joint,

    femur=femur,
    tibia=tibia,

    foot=foot,
)

