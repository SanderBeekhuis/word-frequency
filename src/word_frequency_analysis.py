import re


class WordFrequencyAnalyzer:
    # The existence of this class does not add any value over a couple of methods in a module.
    # It is only created to satisfy the task requirements

    @staticmethod
    def calculate_highest_frequency(text):
        freqencies = WordFrequencyAnalyzer._analyze_text(text)
        return max(freqencies.values())

    @staticmethod
    def calculate_frequency_for_word(text, word):
        frequencies = WordFrequencyAnalyzer._analyze_text(text)
        word = str.lower(word)

        return dict.get(frequencies, word, 0)

    @staticmethod
    def _analyze_text(text):
        lower_text = str.lower(text)
        words = re.findall("[a-zA-Z]+", lower_text)

        frequencies = {}
        for word in words:
            frequencies[word] = frequencies.setdefault(word, 0) + 1

        return frequencies
