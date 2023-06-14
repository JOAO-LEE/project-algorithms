def merge(left, right):

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):

    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:])
    )


def is_anagram(first_string, second_string):
    invalid_value = first_string == '' and second_string == ''
    if invalid_value:
        return (first_string, second_string, False)
    first_word = "".join(merge_sort(first_string.lower()))
    second_word = "".join(merge_sort(second_string.lower()))

    return (first_word, second_word, first_word == second_word)


print(is_anagram("", ""))
