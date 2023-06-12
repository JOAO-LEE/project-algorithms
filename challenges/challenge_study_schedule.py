def study_schedule(permanence_period, target_time):
    invalid_target_time = type(target_time) is not int \
          or target_time is None
    best_time = 0
    if invalid_target_time:
        return None
    for period in permanence_period:
        invalid_permanence_period = type(period[0]) is not int \
           or type(period[1]) is not int
        if invalid_permanence_period:
            return None
        if period[0] <= target_time <= period[1]:
            best_time += 1
    return best_time

# Reference of the Backslash (\) used on lines 2 and 8 below; this is used to continue the condition on the next line.
# https://developer.rhino3d.com/guides/rhinopython/python-statements/#:~:text=You%20cannot%20split%20a%20statement%20into%20multiple%20lines%20in%20Python,continued%20on%20the%20next%20line.


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], None))
