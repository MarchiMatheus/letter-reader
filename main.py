import re

from src.Article import Article

# Process an article
def process():
    
    fileNamePatern = '.*\/(.*).txt'
    filePath = './files/pt/o_lobo_e_a_lua.txt'    

    article = Article(filePath)
    total = article.getTotalLetters()
    vowels = article.getVowelQuantity()
    consonants = article.getConsonantQuantity()

    print('\n###########################################################\n')
    print('Processed numbers for file: ' + re.match(fileNamePatern, filePath).group(1) + '\n')

    print('Vowels: ' + str(vowels) + ', Percentage: %.2f' %((vowels/total)*100) + '%')
    print('Consonants: ' + str(consonants) + ', Percentage: %.2f' %((consonants/total)*100) + '%')
    
    print('\nTotal letters: ' + str(total))

    print('\n###########################################################\n')

# Execute main function
if __name__ == '__main__':
    process()