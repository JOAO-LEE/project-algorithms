def is_palindrome_iterative(word):
    if not word:
        return False

    word_length = len(word)

    if word_length <= 2:
        return True

    word_start = 0
    word_end = word_length - 1

    for index in range(word_length):
        word_start += 1
        word_end -= 1
        if word[word_start] == word[word_end]:
            return True
        else:
            return False


print(is_palindrome_iterative("REVIVER"))
