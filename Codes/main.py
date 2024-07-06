from embeddings import EmbeddingsClass
from api_key import *
def main():
    Config = {'key':API_KEY, 'model':'models/embedding-001'}
    embd = EmbeddingsClass(Config=Config)
    x = embd.generate_embeddings(text="What is your name ? ", pprint=True)   
    print(x)
    

if __name__ == '__main__':
    main()