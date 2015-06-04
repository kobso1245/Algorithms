def reverse(input_text):
    half = (len(input_text) + 1)// 2
    return input_text[half:]+input_text[:half]

def decode(input_text):
    #getting the normal message
    reversed_msg = reverse(input_text)
    #converting the message so we can get the key, alphabet and the encoded message itself
    splitted = reversed_msg.split('~')
    alphabet = splitted[1][:int(splitted[0])]
    key = splitted[1][-int(splitted[2]):]
    message=splitted[1][int(splitted[0]):-int(splitted[2])]
    #converting the coded message to numbers
    indexes_of_coded_message = convert_from_message_to_numbers(message, alphabet)
    #converting the key to numbers
    full_key = key * (len(message) // int(splitted[2])) + key[:(len(message) % int(splitted[2]))]
    indexes_of_key = convert_from_message_to_numbers(full_key, alphabet)
    length_message = len(indexes_of_key)
    #getting the decoded message's indexes
    indexes_of_decoded_message = []
    for i in range(length_message):
        indexes_of_decoded_message.append(indexes_of_coded_message[i] - indexes_of_key[i])
    #turning the decoded message to message with letters
    original_message = from_indexes_to_message(indexes_of_decoded_message, alphabet)
    return original_message

def from_indexes_to_message(indexes, alphabet):
    message = [alphabet[index] for index in indexes]
    return "".join(message)

def convert_from_message_to_numbers(message, alphabet):
    return [alphabet.index(char) for char in message]
print(decode('o?uin uw?stutnfwat?~413~orwa? thfuisnnrsiu'))
