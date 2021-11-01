VOWELS = "aeiouyAEIOUY"


def is_vowel(symbol: chr) -> bool:
    """
        Checks whether the symbol is vowel according to an english alphabet.

        Args:
            symbol: symbol (char)

        Returns:
            True in case the symbol is vowel, False - otherwise.
    """
    if symbol in VOWELS:
        return True
    else:
        return False


def count_vowels(line: str) -> int:
    """
        Count vowels in word.

        Args:
            line: input string

        Returns:
            int, amount of vowels in line according to an english alphabet.
    """
    counter = 0
    for symbol in line:
        if is_vowel(symbol):
            counter += 1
    return counter


def count_relation(line: str) -> float:
    """
        Count mathematical relation of VOWELS_COUNT/SYMBOLS_AMOUNT

        Args:
            line: word

        Returns:
            float, the result of division of VOWELS_COUNT by SYMBOLS_AMOUNT.
    """
    if len(line) == 0:
        return 0.0
    else:
        return (count_vowels(line) * 1.0) / len(line)
