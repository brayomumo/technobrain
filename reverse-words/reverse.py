'''
word: sequence of non-space characters

words separated by atleast one space 

return string of words in reverse order
'''

def solution(sentence: str):
    sent = []
    for word in sentence.split():
        sent.append(word)
    
    return ' '.join(sent[::-1])

assert solution(" This sentence has a leading space") == "space leading a has sentence This"
assert solution("Words   are   separated    by multiple  spaces") == "spaces multiple by separated are Words"
assert solution(" This sentence has a trailing space ") == "space trailing a has sentence This"