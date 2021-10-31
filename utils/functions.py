VOWELS = "aeiouyAEIOUY"

def is_vowel(symbol:chr)->bool:
    if symbol in VOWELS:
        return True
    else:
        return False

def count_vowels(line: str) -> int:
    counter = 0
    for symbol in line:
        if is_vowel(symbol):
            counter+=1
    return counter

def count_relation(line: str) -> float:
    if len(line) == 0:
        return 0.0
    else:
        return (count_vowels(line) * 1.0) / len(line)
