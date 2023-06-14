def is_valid_item(item, position):
    if type(item[position]) != int:
        return False
    elif not item[position] >= 0:
        return False
    else:
        return True


def find_duplicate(nums):
    if nums is None or nums == "" or nums == [] or len(nums) == 1:
        return False

    sorted_nums = sorted(nums)
    array_length = len(nums)
    found_duplicate = False

    for index in range(array_length - 1):
        is_valid = is_valid_item(sorted_nums, index)
        if not is_valid:
            return False
        if sorted_nums[index] == sorted_nums[index + 1]:
            found_duplicate = sorted_nums[index]

    return found_duplicate


print(find_duplicate([1, 3, 4, 2, 77, 77]))
