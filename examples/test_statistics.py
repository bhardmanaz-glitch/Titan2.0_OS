from titan.analysis.measurement import MotionMeasurement
from titan.analysis.statistics import MotionStatistics

measurements = [
    MotionMeasurement(0.0, 0.00, 0.00),
    MotionMeasurement(0.1, 0.11, 0.01),
    MotionMeasurement(0.2, 0.19, -0.01),
]

summary = MotionStatistics.compute(measurements)

print(summary)