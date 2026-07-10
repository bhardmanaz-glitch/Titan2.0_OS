from titan.motion.scheduler import ExecutionScheduler


def test_schedule_returns_matching_items():

    scheduler = ExecutionScheduler()

    stream1 = [1, 2, 3]
    stream2 = ["a", "b", "c"]

    result = list(
        scheduler.schedule(
            stream1,
            stream2,
        )
    )

    assert result == [
        (1, "a"),
        (2, "b"),
        (3, "c"),
    ]

def test_schedule_handles_different_lengths():

    scheduler = ExecutionScheduler()

    stream1 = [1, 2, 3]
    stream2 = ["a"]

    result = list(
        scheduler.schedule(
            stream1,
            stream2,
        )
    )

    assert result == [
        (1, "a"),
        (2, None),
        (3, None),
    ]

def test_schedule_single_stream():

    scheduler = ExecutionScheduler()

    stream = [1, 2, 3]

    result = list(
        scheduler.schedule(stream)
    )

    assert result == [
        (1,),
        (2,),
        (3,),
    ]