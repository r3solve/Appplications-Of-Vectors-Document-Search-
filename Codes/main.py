from embeddings import EmbeddingsClass
from api_key import *
from vectordb import VectorDB


def main():
    Config = {'key':API_KEY, 'model':'models/embedding-001'}
    embd = EmbeddingsClass(Config=Config)
    #Generate Embeddings for a certain text, set pprint=False for detailed response
    x = embd.generate_embeddings(text="What is your name ? ", pprint=True)   
    print(x)
    #Create A vector DB store embeddings ?
    dialogueDb = VectorDB()
    
    #Create A Collection - Like a table in sql
    dialogueDb.create_collection('dialogue')

    #Add Embeddings to the vector db
    dialogueDb.add_to_collection('dialogue', ["Human: Hi my name is rufus, AI:Okay Rufus Nice to meet you! :)", "Human:I am 32 years old, AI:Nice nice :)"])

    res = dialogueDb.query_collection('dialogue', ['How old is the human ?'], topK=1)
    print(res)
    

if __name__ == '__main__':
    main()