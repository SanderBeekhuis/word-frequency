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
def test_calculate_highest_frequency(text, expected):
    assert wfa.WordFrequencyAnalyzer.calculate_highest_frequency(text) == expected


@pytest.mark.parametrize("text,word,expected", [
    ("This is a sentence", "is", 1),
    ("This is a sentence", "not", 0),
    ("The sun shines over the lake", "the", 2),
    ("The sun shines over the lake", "tHe", 2),
])
def test_calculate_frequency_for_word(text, word, expected):
    assert wfa.WordFrequencyAnalyzer.calculate_frequency_for_word(text, word) == expected


@pytest.mark.parametrize("text,n,expectations", [
        (
            "The sun shines over the lake", 3,
            [wfa.WordFrequency("the", 2), wfa.WordFrequency("lake", 1), wfa.WordFrequency("over", 1)]
        ),
        (
            "Some words are created more equal then some other words", 2,
            [wfa.WordFrequency("some", 2), wfa.WordFrequency("words", 2)]
        ),
        (
            "hi ha ho_ha ho\thi hi", 99,
            [wfa.WordFrequency("hi", 3), wfa.WordFrequency("ha", 2), wfa.WordFrequency("ho", 2)]
        ),
    ])
def test_calculate_most_frequent_n_words(text, n, expectations):
    results = wfa.WordFrequencyAnalyzer.calculate_most_frequent_n_words(text, n)

    assert len(results) == len(expectations)
    for result, expectation in zip(results, expectations):
        assert result.word == expectation.word
        assert result.frequency == expectation.frequency
