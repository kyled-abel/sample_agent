from flask import Flask, request
from langchain_openai import ChatOpenAI
import os
import openai

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/addition')
def hello_world():
    operation = request.headers.get('operation')

    output = str(eval(operation))
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)