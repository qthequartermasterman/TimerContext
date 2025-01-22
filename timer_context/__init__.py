from __future__ import __annotations__
import datetime
import time

__version__ = "1.0.0"

class TimerContext:
    """Context manager to time a block of code using a `with` statement.

    Attributes:
        start: The start time.
        end: The end time (if the context manager has exited).
        duration: The duration of the block of code. If the context manager has
            not exited, this will be the duration up to the current time.

    Note:
        Because of the additional overhead of the context manager, this may not
        be the most accurate way to time a block of fast code. For a slow block
        of code, the overhead should be proportionally small.
    """

    start: datetime.datetime
    start_counter: int
    end: datetime.datetime | None
    end_counter: int | None

    def __enter__(self) -> Self:
        self.end = None
        self.end_counter = None
        self.start = datetime.datetime.now()
        self.start_counter = time.perf_counter_ns()
        return self

    def __exit__(self, *args: object, **kwargs: Any) -> None:
        # End the counter first because datetime.datetime.now() takes longer than the perf_counter, and the counter needs to be more precise.
        self.end_counter = time.perf_counter_ns()
        self.end = datetime.datetime.now()

    @property
    def duration_ns(self) -> int:
        """The duration of the block of code, in nanoseconds."""
        return (self.end_counter or time.perf_counter_ns()) - self.start_counter

    @property
    def duration(self) -> float:
        """The duration of the block of code, in milliseconds."""
        return self.duration_ns/1000