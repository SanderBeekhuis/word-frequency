import re
from collections import Counter


class WordFrequencyAnalyzer:
    """
    Provides word frequency analysis methods for a provided text.

    Calculates an intermediate data structure on construction, speeding up subsequent methods on the same text.

    :param text:  The text we want to analyze
    """

    def __init__(self, text: str):
        self.frequencies = WordFrequencyAnalyzer._analyze_text(text)

    @staticmethod
    def _analyze_text(text: str) -> Counter:
        lower_text = str.lower(text)
        words = re.findall("[a-zA-Z]+", lower_text)
        return Counter(words)

    def calculate_highest_frequency(self) -> int:
        """
        :return: The frequency of the most common word in the text
        """
        return max(self.frequencies.values())

    def calculate_frequency_for_word(self, word: str) -> int:
        """
        Calculate the frequency of a word in the text.

        :param word: The word to calculate the frequency of, case-insensitive.
        :return: The frequency of the provided word.
        """
        word = str.lower(word)

        return dict.get(self.frequencies, word, 0)

    def calculate_most_frequent_n_words(self, n: int) -> list['WordFrequency']:
        """
        Calculate a list with the most frequent words in the text.

        :param n: number of entries to be returned.
        :return: the top-`n` most frequent words
        """
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
