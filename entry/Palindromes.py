def is_pallindrome(value):
    length = len(value)
    half_length = length // 2
    for i in range(half_length):
        if value[i] != value[length - i - 1]:
            return False

    return True


def generate_all_combos(input_word):
    resulted_combos = [input_word]
    length = len(input_word)
    for i in range(1, length):
        resulted_combos.append(input_word[i:] + input_word[:i])

    return resulted_combos


# function to run
def check_for_palindromes(input_word):
    combos = generate_all_combos(input_word)
    result = [word for word in combos if is_pallindrome(word)]
    if result == []:
        result = 'NONE'
    return result
