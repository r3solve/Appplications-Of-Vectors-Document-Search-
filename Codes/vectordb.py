import chromadb
from chromadb import Documents, EmbeddingFunction
import chromadb.utils.embedding_functions as embedding_functions
from api_key import *
from embeddings import EmbeddingsClass
from typing import List, Annotated, Any

google_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=API_KEY)

class VectorDB:
    '''
    Args:
        This is initialized with a db configurations,
    Return:
        None is returned if there is a successful initialization
    '''
    def __init__(self) -> None:
        self.client = chromadb.Client()

    @property
    def embeddings_scheme(self):
        '''
        This Lists the embeddings used
        '''
        return google_ef._model_name

    def create_collection(self, name: str) -> None:
        self.client.create_collection(name=name, embedding_function=google_ef)

    def add_to_collection(self, collection_name: str, docs: List[str]) -> None:
        try:
            collection = self.get_collection(collection_name)
            collection.add(
                documents=docs,
                ids=[str(i) for i in range(len(docs))]
            )
        except Exception as e:
            print(e)

    def get_collection(self, name: str) -> chromadb.Collection:
        return self.client.get_collection(name=name)

    def query_collection(self, collection_name: str, query_text: List[str], topK: int = 10) -> Any:
        collection = self.get_collection(collection_name)
        return collection.query(
            query_texts=query_text,
            n_results=topK,
        )

# dialogueDb = VectorDB()

# dialogueDb.create_collection('dialogue')
# dialogueDb.add_to_collection('dialogue', ["Human: Hi my name is rufus, AI:Okay Rufus Nice to meet you! :)", "Human:I am 32 years old, AI:Nice nice :)"])

# res = dialogueDb.query_collection('dialogue', ['How old is the human ?'], topK=1)
# print(res['documents'])
