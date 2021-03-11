import re
from collections import Counter


class WordFrequencyAnalyzer:
    """
    Class that supplies multiple word frequency analysis tools.
    """

    @staticmethod
    def calculate_highest_frequency(text: str) -> int:
        frequency_dict = WordFrequencyAnalyzer._analyze_text(text)
        return max(frequency_dict.values())

    @staticmethod
    def calculate_frequency_for_word(text: str, word: str) -> int:
        frequency_dict = WordFrequencyAnalyzer._analyze_text(text)
        word = str.lower(word)

        return dict.get(frequency_dict, word, 0)

    @staticmethod
    def calculate_most_frequent_n_words(text: str, n: int) -> list['WordFrequency']:
        frequency_dict = WordFrequencyAnalyzer._analyze_text(text)
        frequencies = map(lambda word: WordFrequency(word, frequency_dict[word]), frequency_dict)
        frequencies = sorted(frequencies, key=lambda e: (-e.frequency, e.word))
        return frequencies[:n]

    @staticmethod
    def _analyze_text(text):
        lower_text = str.lower(text)
        words = re.findall("[a-zA-Z]+", lower_text)
        return Counter(words)


class WordFrequency:
    """
    Container class for word and frequency data
    """

    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency
