class Article():
    """ This class processes the file passed in the constructor and executes some operations """

    #Contructor
    def __init__(self, filePath):

        """
        Article constructor
        Creates a Article class that has some information about the given text
        The constructor builds a letter dictionary that will be used for further processing

        Parameters
        ----------
        self : Article class object
        filePath : Path to the file that will be processed
        """

        # Initialize Article class private variables
        self.__letterDictionary = {}
        self.__vowelArray = ['a', 'e', 'i', 'o', 'u', 'á', 'à', 'â', 'ã', 'é', 'ê', 'í', 'ó', 'õ', 'ú']

        with open(filePath, encoding="utf-8") as file:

            for line in file:
                for letter in line:

                    # Check if letter variable is actually a letter
                    if letter.isalpha():

                        # Normalize the letter
                        lowerLetter = letter.lower()

                        if lowerLetter in self.__letterDictionary.keys():
                            self.__letterDictionary[lowerLetter] += 1
                    
                        else:
                            self.__letterDictionary[lowerLetter] = 1

    
    def getDictionary(self):

        """
        Returns the letter dictionary

        Parameters
        ----------
        self : Article class object
        """

        return self.__letterDictionary

    def getTotalLetters(self):

        """
        Returns the total amount of letters in the article

        Parameters
        ----------
        self : Article class object
        """

        totalLetters = 0

        for letter in self.__letterDictionary:
            totalLetters += self.__letterDictionary[letter]

        return totalLetters

    def getVowelQuantity(self):

        """
        Returns the quantity of vowels in the article

        Parameters
        ----------
        self : Article class object
        """

        totalVowels = 0

        for vowel in self.__vowelArray:
            if vowel in self.__letterDictionary.keys():
                totalVowels += self.__letterDictionary[vowel]

        return totalVowels

    def getConsonantQuantity(self):

        """
        Returns the quantity of consonants in the article

        Parameters
        ----------
        self : Article class object
        """

        totalConsonants = 0

        for letter in self.__letterDictionary:
            if letter not in self.__vowelArray:
                totalConsonants += self.__letterDictionary[letter]

        return totalConsonants