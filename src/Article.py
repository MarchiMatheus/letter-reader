
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

        self.letterDictionary = {}

        with open(filePath, encoding="utf-8") as file:

            for line in file:
                for letter in line:

                    if letter in self.letterDictionary.keys():
                        self.letterDictionary[letter] += 1
                    
                    else:
                        self.letterDictionary[letter] = 1

    
    def getDictionary(self):

        """
        Returns the letter dictionary
        """

        return self.letterDictionary