import re

class WordFrequencyAnalyzer:
    # The existence of this class does not add any value over a couple of methods in a module.
    # It is only created to satisfy the task requirements

    @staticmethod
    def calculate_highest_frequency(text):
        lower_text = str.lower(text)
        words = re.findall("[a-zA-Z]+", lower_text)

        frequencies = {}
        for word in words:
            frequencies[word] = frequencies.setdefault(word, 0) + 1

        return max(frequencies.values())
