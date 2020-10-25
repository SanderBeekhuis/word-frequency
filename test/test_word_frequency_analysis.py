import src.word_frequency_analysis as wfa
import pytest


@pytest.mark.parametrize("text,expected", [
        ("oneWord other words", 1),
        ("two two", 2),
        ("tabs\ttabs", 2),
        ("newline\nnewline", 2),
        ("case indifference Hi hi HI", 3),
        ("non-whitespace-separator non", 2),
        ("The sun shines over the lake", 2)
    ])
def calculate_highest_frequency_test(text, expected):
    assert wfa.WordFrequencyAnalyzer.calculate_highest_frequency(text) == expected


@pytest.mark.parametrize("text,word,expected", [
    ("This is a sentence", "is", 1),
    ("This is a sentence", "not", 0),
    ("The sun shines over the lake", "the", 2),
    ("The sun shines over the lake", "tHe", 2),
])
def test(text, word, expected):
    assert wfa.WordFrequencyAnalyzer.calculate_frequency_for_word(text, word) == expected
