import re

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
        self.__filePath = filePath
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

        Returns
        -------
        int : The letter dictionary
        """

        return self.__letterDictionary

    def getTotalLetters(self):

        """
        Returns the total amount of letters in the article

        Parameters
        ----------
        self : Article class object

        Returns
        -------
        int : The total letters in the article
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

        Returns
        -------
        int : The total of vowels
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

        Returns
        -------
        int : The total of consonants
        """

        totalConsonants = 0

        for letter in self.__letterDictionary:
            if letter not in self.__vowelArray:
                totalConsonants += self.__letterDictionary[letter]

        return totalConsonants

    def getLetterQuantity(self, letter):

        """
        Returns the quantity of the given letter

        Parameters
        ----------
        self : Article class object
        letter: Letter to get the quantity

        Returns
        -------
        int : The quantity of the given letter in the article or -1 if the letter isn't in the article
        """

        lowerLetter = letter.lower()

        if lowerLetter not in self.__letterDictionary.keys():
            return -1

        return self.__letterDictionary[lowerLetter]

    def showInformation(self):

        """
        Prints the article information

        Parameters
        ----------
        self : Article class object
        """

        fileNamePatern = '.*\/(.*).txt'

        total = self.getTotalLetters()
        vowels = self.getVowelQuantity()
        consonants = self.getConsonantQuantity()

        print('\n###########################################################\n')
        print('Processed numbers for file: ' + re.match(fileNamePatern, self.__filePath).group(1) + '\n')

        print('Vowels: ' + str(vowels) + ', Percentage: %.2f' %((vowels/total)*100) + '%')
        print('Consonants: ' + str(consonants) + ', Percentage: %.2f' %((consonants/total)*100) + '%')
        
        print('\nTotal letters: ' + str(total))

        print('\n###########################################################\n')