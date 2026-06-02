from app.text_stats import char_count, top_words, word_count


def test_word_count_basic():
    assert word_count("hello world") == 2


def test_word_count_empty():
    assert word_count("") == 0


def test_char_count_with_and_without_spaces():
    assert char_count("hi, this is kamal!") == 18
    assert char_count("hi, this is kamal!", include_spaces=False) == 15


def test_top_words():
    text = "the cat sat on the mat in the end"
    result = top_words(text, n=2)
    assert result[0] == ("the", 3)
    assert len(result) == 2


def test_top_words_punc_case_sensitive():
    result = top_words("Dog. dog doG!", n=1)
    assert result == [("dog", 3)]
