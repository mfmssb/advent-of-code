from pathlib import Path
from typing import Any

# %%
def parse_data(data_path: str) -> tuple[list[str], list[str]]:    
    data = Path(data_path).read_text()
    data = data.split("\n\n")
    intervals, ids = data[0].splitlines(), data[1].splitlines()
    return intervals, ids


def is_in_interval(x: str, interval: str) -> bool:
    """
    Check if x is in "a-b", b included
    """
    from_, to_ = interval.split("-")
    return int(from_) <= int(x) <= int(to_)

def p1(data_path: str) -> int:
    """
    Loop through all ids and intervals and check if id is within
    any intervals.
    """
    intervals, ids = parse_data(data_path)
    num_fresh = 0
    for id_ in ids:
        for int_ in intervals:
            if is_in_interval(x=id_, interval=int_):
                num_fresh += 1
                break
    return num_fresh

def convert_intervals_to_numbers(interval1: str, interval2: str) -> tuple[int, int, int, int]:
    int1_low, int1_high = interval1.split(sep="-")
    int2_low, int2_high = interval2.split(sep="-")

    return int(int1_low), int(int1_high), int(int2_low), int(int2_high)

def is_intersecting(interval1: str, interval2: str) -> bool:
    """
    Determine whether two given intervals are intersecting or not.
    """
    int1_low, int1_high, int2_low, int2_high = convert_intervals_to_numbers(interval1, interval2)

    if int1_low <= int2_low <= int1_high or int1_low <= int2_high <= int1_high:
        return True
    return False

def make_new_interval(interval1: str, interval2: str) -> str:
    """
    Given that the intervals are intersecting, reduce them to one by
    setting the lower and higher value with min and max.
    "4-8" and "5-10" -> "4-10"
    """
    int1_low, int1_high, int2_low, int2_high = convert_intervals_to_numbers(interval1, interval2)

    new_low: int = min(int1_low, int2_low)
    new_high: int = max(int1_high, int2_high)

    return f"{new_low}-{new_high}"


def reduce_intervals_once(intervals: list[str]) -> list[str]:
    """
    Make a dictionary of all intervals and set True if the interval has been reduced.
    The reduced interval is stored in new_intervals.
    If an interval is not intersected by another, it is added to new_intervals
    """
    intervals_with_intersections: dict[str, bool] = dict.fromkeys(intervals, False)

    new_intervals= []
    for interval1 in intervals:
        for interval2 in intervals:
            if interval1 != interval2 and is_intersecting(interval1, interval2):
                intervals_with_intersections[interval1] = True
                intervals_with_intersections[interval2] = True
                new_intervals.append(make_new_interval(interval1, interval2))

    new_intervals= list(set(new_intervals))  # keep all unique intervals
    for interval, is_intersected in intervals_with_intersections.items():
        if not is_intersected:
            new_intervals.append(interval)

    return new_intervals

def reduce_intervals_as_much_as_possible(intervals: list[str]) -> list[str]:
    """
    Keep reducing until reduce_intervals_once() produces no more unique intervals.
    """
    cont = True
    while cont:
        reduced_intervals = reduce_intervals_once(intervals)
        if set(intervals) == set(reduced_intervals):
            cont = False
        intervals = reduced_intervals.copy()

    return intervals

# %%
def num_fresh_id_from_reduced_intervals(reduced_intervals: list[str]) -> int:
    """
    Calculate the number of ids contained in all reduced intervals.
    "4-6" -> 3
    """
    total = 0
    for int_ in reduced_intervals:
        min_, max_ = int_.split(sep="-")
        total += int(max_) - int(min_) + 1
    return total


# %%
def p2(data_path: str) -> int:
    intervals, ___ = parse_data(data_path)

    reduced_intervals = reduce_intervals_as_much_as_possible(intervals)
    
    return num_fresh_id_from_reduced_intervals(reduced_intervals)

# %%
print(p1(data_path="aoc_2025/05/data/data1.txt"))
print(p2(data_path="aoc_2025/05/data/data1.txt"))
# %%
%timeit p2(data_path="aoc_2025/05/data/data1.txt")
