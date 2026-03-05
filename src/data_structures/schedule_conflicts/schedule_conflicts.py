from datetime import datetime
from typing import List, Tuple


def find_schedule_conflicts(intervals: list[tuple[str, str]]) -> list[tuple[str, str]]:
    if intervals == 0:
        return []
    result = []
    num_intervals = [tuple(datetime.strptime(x, "%H:%M").hour * 60 + datetime.strptime(x, "%H:%M").minute for x in t) for t in intervals]

    for i in range(len(num_intervals)):
        for j in range(i + 1, len(num_intervals)):
            a, b = num_intervals[i], num_intervals[j]
            if max(a[0], b[0]) < min(a[1], b[1]):
                result.append((intervals[i], intervals[j]))

    return result


print(find_schedule_conflicts([("09:00", "10:00"), ("09:30", "11:00"), ("11:00", "12:00")]))