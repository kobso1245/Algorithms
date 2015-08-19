def hash_calculator(text):
    length = len(text)
    hash_val = 0
    for letter in text[::-1]:
        hash_val = (hash_val*101 + ord(letter)) % 2000000

    return hash_val % 2000000

def hash_recalculation(old_hash, old_letter, new_letter, length):
    new_hash = 0
    new_hash = (101 * (old_hash - (ord(old_letter)*(101**(length - 1)))%2000000) + ord(new_letter)) % 2000000

    return new_hash


def get_indexes(haystack, needle):
    indexes = []
    length_needle = len(needle)
    hash_needle = hash_calculator(needle)
    curr_hash = hash_calculator(haystack[:length_needle])
    for i in range(length_needle,len(haystack)):
        print(curr_hash, hash_needle)
        
        if curr_hash == hash_needle:
            print(curr_hash, hash_needle)
            if haystack[i - length_needle, length_needle] == needle:
                indexes.append(i-length_needle)
        curr_hash = hash_recalculation(curr_hash, haystack[i - length_needle], haystack[i], length_needle)
    return indexes


def main():
    print(get_indexes("thequickbrownfoxjumpsoverthelazydogthedogwassoamused", "dog"))

main()
