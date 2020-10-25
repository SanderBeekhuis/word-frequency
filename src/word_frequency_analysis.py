import re


class WordFrequencyAnalyzer:
    # The existence of this class does not add any value over a couple of methods in a module.
    # It is only created to satisfy the task requirements

    @staticmethod
    def calculate_highest_frequency(text):
        frequency_dict = WordFrequencyAnalyzer._analyze_text(text)
        return max(frequency_dict.values())

    @staticmethod
    def calculate_frequency_for_word(text, word):
        frequency_dict = WordFrequencyAnalyzer._analyze_text(text)
        word = str.lower(word)

        return dict.get(frequency_dict, word, 0)

    @staticmethod
    def calculate_most_frequent_n_words(text, n):
        frequency_dict = WordFrequencyAnalyzer._analyze_text(text)
        frequencies = map(lambda word: WordFrequency(word, frequency_dict[word]), frequency_dict)
        frequencies = sorted(frequencies, key=lambda e: (-e.frequency, e.word))
        return frequencies[:n]

    @staticmethod
    def _analyze_text(text):
        lower_text = str.lower(text)
        words = re.findall("[a-zA-Z]+", lower_text)

        frequency_dict = {}
        for word in words:
            frequency_dict[word] = frequency_dict.setdefault(word, 0) + 1

        return frequency_dict


class WordFrequency:
    # It is better to use a named tuple here i.s.o coding this data-class myself.
    # However that would offend the task requirements

    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency
