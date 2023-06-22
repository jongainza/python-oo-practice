"""Word Finder: finds random words from a dictionary."""
import random
import parse


class WordFinder:
    """reads the file and print text with number of words in the file"""

    def __init__(self, path):
        cus = open(path)
        self.words = self.parse(cus)
        print(f"{len(self.words)} words read")

    def parse(self, cus):
        """takes out line separator and empty spaces at beggining and end of the word"""
        return [w.strip() for w in cus]

    def give_me_words(self):
        """prints out all the words in the file.DON'T USE IT!!!"""
        print(self.words)

    def random_word(self):
        """Selects a random word from the list"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Excludes words starting with '#'"""

    def parse(self, cus):
        return [w.strip() for w in cus if w.strip() and not w.startswith("#")]

    # wf = WordFinder("joninakigainza/desktop/sprigboard/bootcamp_practices/python-oo-practice/words.txt")
    # wf = WordFinder("words.txt")
