import os
import google.generativeai as genai
from api_key import *

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

while 1:
    inp = input("Ask Me something ? ")
    response = model.generate_content(inp)
    print(response.text)


