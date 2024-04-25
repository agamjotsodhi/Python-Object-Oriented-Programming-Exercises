"""Word Finder: finds random words from a dictionary."""
import random

class WordPicker:
    def __init__(self, path):
        self.words = self.read_words(path)

    def read_words(self, path):
        words = []
        with open(path, 'r') as file:
            for line in file:
                words.append(line.strip())
        return words

    def random(self):
        return random.choice(self.words)

if __name__ == "__main__":
    path = "words.txt"  
    word_picker = WordPicker(path)
    print("Number of words read:", len(word_picker.words))
    print("Random word:", word_picker.random())
    

    