import time
from timer_context import TimerContext
from hypothesis import strategies as st
import hypothesis
import pytest

# Define a common strategy for sleep times
sleep_time_strategy = st.floats(min_value=1e-9, max_value=1e-2)


def test_initialization() -> None:
    """Test that TimerContext initializes correctly, setting start time and performance counter."""
    with TimerContext() as timer:
        assert timer.start is not None
        assert timer.end is None
        assert timer.start_counter > 0


@hypothesis.given(sleep_time=sleep_time_strategy)
def test_duration_calculation(sleep_time: float) -> None:
    """Test that TimerContext calculates the duration correctly for a given block of code."""
    with TimerContext() as timer:
        time.sleep(sleep_time)
        duration = timer.duration
        assert pytest.approx(duration, rel=0.01) == sleep_time * 1000  # Allow small relative tolerance


def test_end_values() -> None:
    """Test that TimerContext sets end values correctly after exiting the context and the duration remains constant."""
    with TimerContext() as timer:
        time.sleep(0.1)
    duration_after_exit = timer.duration
    assert timer.end is not None
    assert timer.end_counter is not None
    assert duration_after_exit > 0
    # Ensure duration does not change after the context has ended
    assert pytest.approx(duration_after_exit, rel=0.01) == timer.duration


@hypothesis.given(sleep_time_outer=sleep_time_strategy, sleep_time_inner=sleep_time_strategy)
def test_nested_contexts(sleep_time_outer: float, sleep_time_inner: float) -> None:
    """Test that nested TimerContext instances work correctly and track independent durations."""
    with TimerContext() as outer_timer:
        time.sleep(sleep_time_outer)
        with TimerContext() as inner_timer:
            time.sleep(sleep_time_inner)
        assert pytest.approx(inner_timer.duration, rel=0.01) == sleep_time_inner * 1000
    assert pytest.approx(outer_timer.duration, rel=0.01) == (sleep_time_outer + sleep_time_inner) * 1000


@hypothesis.given(sleep_time=sleep_time_strategy)
def test_duration_consistency(sleep_time: float) -> None:
    """Test that duration in milliseconds is consistent with duration in nanoseconds."""
    with TimerContext() as timer:
        time.sleep(sleep_time)
    assert pytest.approx(timer.duration, rel=0.01) == timer.duration_ns / 1000


@hypothesis.given(sleep_time=sleep_time_strategy)
def test_exception_handling(sleep_time: float) -> None:
    """Test that TimerContext tracks time correctly even if an exception is raised in the block."""
    try:
        with TimerContext() as timer:
            time.sleep(sleep_time)
            raise ValueError("Intentional error")
    except ValueError:
        pass
    assert timer.end is not None
    assert pytest.approx(timer.duration, rel=0.01) == sleep_time * 1000
