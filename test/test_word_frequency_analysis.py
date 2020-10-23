import src.word_frequency_analysis as wfa
import pytest


@pytest.mark.parametrize("text,highest_freq", [
        ("oneWord other words", 1),
        ("two two", 2),
        ("tabs\ttabs", 2),
        ("newline\nnewline", 2),
        ("case indifference Hi hi HI", 3),
        ("non-whitespace-separator non", 2),
        ("The sun shines over the lake", 2)
    ])
def test_word_frequency_analysis(text, highest_freq):
    assert wfa.WordFrequencyAnalyzer.calculate_highest_frequency(text) == highest_freq;