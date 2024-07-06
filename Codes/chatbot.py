import os
import google.generativeai as genai
from loader import load_text_file
from vectordb import VectorDB
from embeddings import EmbeddingsClass

from api_key import *

Config = {"key":API_KEY, "model":"models/text-embedding-004"}

#Create A new Vector DB.
DialogueDb = VectorDB()

#Initialize the embededing fuction
embd = EmbeddingsClass(Config)

genai.configure(api_key=API_KEY)

#Load the Dialogue Messages
dialogue = load_text_file('doc.txt')

#Create A collection to store the vectors of dialgues
DialogueDb.create_collection('dialogue')

#Initialize the Gemini LLM
model = genai.GenerativeModel('gemini-1.5-flash')

#Fuctions to generate a query_prompt
def make_prompt(user_prompt: str, context: str) -> str:
    return f"""
        You are a Q&A Conversational chatbot that answers questions only from a given context window.
        The context window is a dialgoue script between people. 
        If you can't find the answer in the given context window, say you don't know and that you're sorry you don't know the answer to that question.
        Now, here is the context: {context}
        Answer this question: {user_prompt}
        """

DialogueDb.add_to_collection('dialogue',dialogue)



while 1:
    inp = input("Ask Me something (Ask)>> ")
    res = DialogueDb.query_collection('dialogue', inp)
    response = model.generate_content(make_prompt(inp, res.get('documents')))
    print(response.text)

