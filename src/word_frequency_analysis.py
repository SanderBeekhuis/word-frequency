import re
from collections import Counter


class WordFrequencyAnalyzer:
    """
    Class that supplies multiple word frequency analysis tools.
    """

    def __init__(self, text: str):
        self.frequencies = WordFrequencyAnalyzer._analyze_text(text)

    @staticmethod
    def _analyze_text(text: str) -> Counter:
        lower_text = str.lower(text)
        words = re.findall("[a-zA-Z]+", lower_text)
        return Counter(words)

    def calculate_highest_frequency(self) -> int:
        return max(self.frequencies.values())

    def calculate_frequency_for_word(self, word: str) -> int:
        word = str.lower(word)

        return dict.get(self.frequencies, word, 0)

    def calculate_most_frequent_n_words(self, n: int) -> list['WordFrequency']:
        frequencies = (WordFrequency(word, self.frequencies[word]) for word in self.frequencies)
        frequencies = sorted(frequencies, key=lambda wf: (-wf.frequency, wf.word))
        return frequencies[:n]


class WordFrequency:
    """
    Container class for word and frequency data
    """

    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency
