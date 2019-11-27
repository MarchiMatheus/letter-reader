import re
import operator

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

        self.__simpleVowelArray = ['a', 'e', 'i', 'o', 'u']
        self.__vowelArray = ['a', 'e', 'i', 'o', 'u', 'á', 'à', 'â', 'ã', 'é', 'ê', 'í', 'ó', 'õ', 'ú']

        self.__accentedLetterArray = ['á', 'à', 'â', 'ã', 'é', 'ê', 'í', 'ó', 'õ', 'ú']

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

    def getAccentedLetterQuantity(self):

        """
        Returns the quantity of accented letters in the article

        Parameters
        ----------
        self : Article class object

        Returns
        -------
        int : The total of accented letters
        """

        totalAccentedLetters = 0

        for letter in self.__letterDictionary:
            if letter in self.__accentedLetterArray:
                totalAccentedLetters += self.__letterDictionary[letter]

        return totalAccentedLetters

    def getMostUsedVowel(self, considerAccent):

        """
        Returns the most used vowel in the article

        Parameters
        ----------
        self : Article class object
        considerAccent : Boolean to consider accented vowels or not

        Returns
        -------
        int : The most used vowel in the article
        """

        vowel = ''
        mostUsedVowel = -1

        if considerAccent:
            for v in self.__vowelArray:
                if v in self.__letterDictionary.keys() and self.__letterDictionary[v] > mostUsedVowel:
                    vowel = v
                    mostUsedVowel = self.__letterDictionary[v]

        else :
            for v in self.__simpleVowelArray:
                if v in self.__letterDictionary.keys() and self.__letterDictionary[v] > mostUsedVowel:
                    vowel = v
                    mostUsedVowel = self.__letterDictionary[v]

        return vowel, mostUsedVowel

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

    def showVowelInformation(self, considerAccent):

        """
        Prints the vowel article information

        Parameters
        ----------
        self : Article class object
        """

        total = self.getTotalLetters()
        
        letterA = self.__letterDictionary['a']
        letterE = self.__letterDictionary['e']
        letterI = self.__letterDictionary['i']
        letterO = self.__letterDictionary['o']
        letterU = self.__letterDictionary['u']

        #Recalculates if must consider vowels accentuated
        if considerAccent:

            if 'á' in self.__letterDictionary.keys(): letterA += self.__letterDictionary['á']
            if 'à' in self.__letterDictionary.keys(): letterA += self.__letterDictionary['à']
            if 'â' in self.__letterDictionary.keys(): letterA += self.__letterDictionary['â']
            if 'ã' in self.__letterDictionary.keys(): letterA += self.__letterDictionary['ã']

            if 'é' in self.__letterDictionary.keys(): letterE += self.__letterDictionary['é']
            if 'ê' in self.__letterDictionary.keys(): letterE += self.__letterDictionary['ê']

            if 'í' in self.__letterDictionary.keys(): letterI += self.__letterDictionary['í']

            if 'ó' in self.__letterDictionary.keys(): letterO += self.__letterDictionary['ó']
            if 'õ' in self.__letterDictionary.keys(): letterO += self.__letterDictionary['õ']

            if 'ú' in self.__letterDictionary.keys(): letterU += self.__letterDictionary['ú']

        print('\n###########################################################\n')

        print('Letter A: ' + str(letterA) + ', Percentage: %.2f' %((letterA/total)*100) + '%')
        print('Letter E: ' + str(letterE) + ', Percentage: %.2f' %((letterE/total)*100) + '%')
        print('Letter I: ' + str(letterI) + ', Percentage: %.2f' %((letterI/total)*100) + '%')
        print('Letter O: ' + str(letterO) + ', Percentage: %.2f' %((letterO/total)*100) + '%')
        print('Letter U: ' + str(letterU) + ', Percentage: %.2f' %((letterU/total)*100) + '%')

        print('\nTotal letters: ' + str(total))

        print('\n###########################################################\n')