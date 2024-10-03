from flask import Flask
from langchain_openai import ChatOpenAI
import os
import openai
import requests

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/')
def hello_world():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    output = llm.invoke("What would be the AI equivalent of Hello World?")
    
    response = requests.get('http://agent1:5001/')
    return f"Output from master agent: {output.content}, Output from agent1: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)