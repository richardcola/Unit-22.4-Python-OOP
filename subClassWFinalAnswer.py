import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    
    def __init__(self, file_path):
        """
        Initialize the WordFinder with a path to a file containing words.
        
        Parameters:
        - file_path (str): The path to the file containing words.
        """
        self.words = self.read_words(file_path)
    
    def read_words(self, file_path):
        """
        Read words from the file and return them as a list.
        
        Parameters:
        - file_path (str): The path to the file containing words.
        
        Returns:
        - list: A list of words read from the file.
        """
        with open(file_path, 'r') as file:
            words = [word.strip() for word in file if word.strip() and not word.startswith("#")]
        return words
    
    def random(self):
        """
        Return a random word from the list of words.
        
        Returns:
        - str: A random word from the list.
        """
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary, excluding blanks and commented words."""
    
    def read_words(self, file_path):
        """
        Read words from the file, excluding blanks and commented words, and return them as a list.
        
        Parameters:
        - file_path (str): The path to the file containing words.
        
        Returns:
        - list: A list of words read from the file, excluding blanks and commented words.
        """
        with open(file_path, 'r') as file:
            words = [word.strip() for word in file if word.strip() and not word.startswith("#")]
        return words


# Test the SpecialWordFinder class
swf = SpecialWordFinder("/Users/student/words.txt")
print(len(swf.words), "words read")

print(swf.random())
print(swf.random())
print(swf.random())
print(swf.random())
