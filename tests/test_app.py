
from app import analyze_text


def test_word_count():
    results = analyze_text("Python is fun")
    assert results["word_count"] == 3


def test_character_count():
    results = analyze_text("Hello world")
    assert results["character_count"] == 11


def test_sentence_count():
    results = analyze_text("Hello! How are you? I am fine.")
    assert results["sentence_count"] == 3


def test_average_word_length():
    results = analyze_text("Cat dog")
    assert results["average_word_length"] == 3.0


def test_empty_text():
    results = analyze_text("")
    assert results["word_count"] == 0
    assert results["character_count"] == 0
    assert results["sentence_count"] == 0
    assert results["average_word_length"] == 0
