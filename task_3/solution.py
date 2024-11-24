def normalize_intervals(intervals):
    """Normalizes a list of intervals, e.g. a student opens two tabs at the same time"""
    normalized_list = []
    start = intervals[0]
    end = intervals[1]
    for i in range(2, len(intervals), 2):
        new_start = intervals[i]
        new_end = intervals[i + 1]
        if new_start > end:
            normalized_list.append(start)
            normalized_list.append(end)
            start = new_start
            end = new_end
        if new_end > end:
            end = new_end

    normalized_list.append(start)
    normalized_list.append(end)

    return normalized_list


def appearance(intervals: dict[str, list[int]]) -> int:
    """Returns the appearance time of students and tutors at a lesson"""
    intervals = [normalize_intervals(interval) for interval in intervals.values()]

    appearance_time = 0

    while all(intervals):
        min_end = intervals[0][1]
        max_start = intervals[0][0]
        from_list = intervals[0]
        for i in intervals[1:]:
            if i[1] < min_end:
                min_end = i[1]
                from_list = i
            if i[0] > max_start:
                max_start = i[0]
        interval_len = min_end - max_start
        if interval_len > 0:
            appearance_time += interval_len
        from_list.pop(0)
        from_list.pop(0)

    return appearance_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
