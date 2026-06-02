from collections import Counter


def word_count(text: str) -> int:
    """Number of whatspace separated words"""
    return len(text.split())


def char_count(text: str, include_spaces: bool = True) -> int:
    """Number of characters, optionally ignoring spaces"""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """n Most common words without punctuations"""
    words = [w.lower().strip(".,!?;:") for w in text.split()]
    words = [w for w in words if w]

    return Counter(words).most_common(n)
