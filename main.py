from src.Article import Article

# Process an article
def process():
    
    filePath = './files/pt/o_lobo_e_a_lua.txt'

    article = Article(filePath)
    print(article.getDictionary())

# Execute main function
if __name__ == '__main__':
    process()