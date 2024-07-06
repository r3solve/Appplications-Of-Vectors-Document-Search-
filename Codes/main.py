from embeddings import EmbeddingsClass

def main():
    Config = {'key':"AIzaSyBZa7h0sSf_7saJ6SSc5t6S5SiIbUye2-c", 'model':'models/embedding-001'}
    embd = EmbeddingsClass(Config=Config)
    x = embd.generate_embeddings(text="What is your name ? ", pprint=True)   
    print(x)
    

if __name__ == '__main__':
    main()