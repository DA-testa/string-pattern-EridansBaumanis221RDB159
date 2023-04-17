# python3
import hashlib

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open('tests/06', 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    return pattern, text
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = hashlib.sha256(pattern.encode()).hexdigest()
    text_hash = hashlib.sha256(text.encode()).hexdigest()
    occurrences = []
    for x in range(text_length - pattern_length +1):
        if pattern_hash == hashlib.sha256(text[x:x+pattern_length].encode()).hexdigest():
            if pattern == text[x:x+pattern_length]
            occurrences.append(x)
        if x < text_length - pattern_length:
            text_hash = hashlib.sha256(text[x+1:x+pattern_length+1].encode()).hexdigest():
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
