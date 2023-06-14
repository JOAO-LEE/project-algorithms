def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


def is_anagram(first_string, second_string):
    invalid_value = first_string == "" and second_string == ""
    if invalid_value:
        return (first_string, second_string, False)
    first_word = "".join(quicksort(first_string.lower()))
    second_word = "".join(quicksort(second_string.lower()))

    return (first_word, second_word, first_word == second_word)


# Reference of the quick-sort algorithm used above.
# https://www.geeksforgeeks.org/python-program-for-quicksort/

print(is_anagram("ababc", "babac"))
