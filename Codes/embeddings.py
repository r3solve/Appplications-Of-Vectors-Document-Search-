import google.generativeai as genai
import typing
import numpy as np
import chromadb


class EmbeddingsClass:
    def __init__(self, Config:dict) -> None:
        """
        The onfiguraion dict should be provided as follows
        config = {
        "key":'xxxxxxxxxxxxxxxxxxxxxxxx'
        "model" :'text/divinci',
        }
        }
        """
        self.Config = Config
        genai.configure(api_key=Config.get('key'))
        self.text = ''

    def generate_embeddings(self, text, pprint=True) -> list[int]| None:
        self.text = text 
        embedding = genai.embed_content(
        model=self.Config.get('model'),
        content=text,
        task_type="retrieval_document"
        )
        if embedding is None:
            raise ValueError("Un able to Generate Embeddings")
        embedding['embedding'] = np.array(embedding['embedding'])
        
        if pprint:
            np.set_printoptions(threshold=10)

        return {"text":self.text, 'embedding': embedding['embedding']}
            

        # return embedding
    
    def get_raw_text(self) -> str | ValueError:
        if len(self.text) == 0:
            raise ValueError("None text passed for Processings")
        return self.text

