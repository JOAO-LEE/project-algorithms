def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if len(word) < 2:
        return True

    if low_index >= high_index:
        return True

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False


print(is_palindrome_recursive("abbsssawa", 0, len("abbsssawa") - 1))
