def hash_calculator(text):
    length = len(text)
    hash_val = 0
    multiplier = 1
    for letter in text[::-1]:
        hash_val = (hash_val + ord(letter) * multiplier) % 2000000
        multiplier = (multiplier * 101) % 2000000

    return hash_val


def hash_recalculation(old_hash, old_letter, new_letter, length):
    new_hash = 0
    new_hash = 101 * (old_hash - (101**(length - 1)) *
                      ord(old_letter)) + ord(new_letter)
    return new_hash % 2000000


def get_indexes(haystack, needle):
    indexes = []
    length_needle = len(needle)
    hash_needle = hash_calculator(needle)
    curr_hash = hash_calculator(haystack[:length_needle])
    for i in range(length_needle, len(haystack)):
        if curr_hash == hash_needle:
            if haystack[i - length_needle:i] == needle:
                indexes.append(i - length_needle)
        curr_hash = hash_recalculation(
            curr_hash,
            haystack[
                i - length_needle],
            haystack[i],
            length_needle)
    return indexes


def main():
    haystack = input()
    needle = input()
    res = get_indexes(haystack, needle)
    for index in res:
        print(index)

main()
