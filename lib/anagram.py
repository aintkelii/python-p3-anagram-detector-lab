# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        for candidate in word_list:
            lower_candidate = candidate.lower()
            if lower_candidate != self.word and sorted(lower_candidate) == sorted(self.word):
                matches.append(candidate)
        return matches