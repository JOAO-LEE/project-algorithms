def study_schedule(permanence_period, target_time):
    invalid_target_time = type(target_time) is not int
    best_time = 0
    if target_time == invalid_target_time:
        return None
    for period in permanence_period:
        invalid_permanence_period = type(period[0]) is not int \
            or type(period[1]) is not int
        if invalid_permanence_period:
            return None
        if period[0] <= target_time <= period[1]:
            best_time += 1
    return best_time


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
