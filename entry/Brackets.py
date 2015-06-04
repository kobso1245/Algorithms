OPENING_BRACKETS = "{[("
CLOSING_BRACKETS = "}])"

def validate(input_string):
    already_read_brackets = []
    curr = -1
    written = False
    result = []
    tempo_string=''


    for char in input_string:
        curr+=1
        if already_read_brackets == [] and curr != 0:
            return False
        if char in OPENING_BRACKETS:
            current_bracket_index_in_OPENING_BRACKETS = OPENING_BRACKETS.index(char)
            if already_read_brackets!= []:
                top_of_stack_index_in_OPENING_BRACKETS = OPENING_BRACKETS.index(already_read_brackets[-1])
                #removing {{.. and ((.. and [[.. options
                if already_read_brackets[-1] == char:
                    return False
                #removing ({.. and ({.. and ([.. and [{ and ..you get it.. and {(.. options
                if current_bracket_index_in_OPENING_BRACKETS < top_of_stack_index_in_OPENING_BRACKETS or current_bracket_index_in_OPENING_BRACKETS - top_of_stack_index_in_OPENING_BRACKETS == 2:
                    return False
                else:
                    if written == False:
                        result.append((int(tempo_string), len(already_read_brackets)))
                        tempo_string=''
                        written=True
                    already_read_brackets.append(char)
            else:
                tempo_string=''
                already_read_brackets.append(char)

        elif char in CLOSING_BRACKETS:
            current_bracket_index_in_OPENING_BRACKETS = CLOSING_BRACKETS.index(char)
            if already_read_brackets != []:
                top_of_stack_index_in_OPENING_BRACKETS = OPENING_BRACKETS.index(already_read_brackets[-1])
                if top_of_stack_index_in_OPENING_BRACKETS != current_bracket_index_in_OPENING_BRACKETS:
                    return False
                else:
                    if written == False:
                        result.append((int(tempo_string), len(already_read_brackets)))
                        tempo_string=''
                        written=True
                    
                    already_read_brackets.pop()
            else:
                return False
        elif char in '0123456789':
            if already_read_brackets == []:
                return False
            else:
                written=False
                tempo_string+=char
        else:
            return False
        
    if already_read_brackets != []:
        return False

    return result

#function to run
def calc(input_string):
    final_sum = 0
    res = validate(input_string)
    if res == False:
        return 'NO'
    else:
        for tple in res:
            final_sum+=tple[0]*(2 ** (tple[1]-1))

    return final_sum
