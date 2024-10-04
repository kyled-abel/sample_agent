from flask import Flask
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
import os
import openai
import re
import requests

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]
input = "1+1+2+3=?"

@app.route('/')
def hello_world():
    llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
    tools=[]

    examples = [
        {
            "question": "1+1=?",
            "answer": "Step1. (1+1)"
        },
        {
            "question": "1+1*2=?",
            "answer": "Step1. (1*2)\nStep2. (1+answer)"
        },
        {
            "question": "(1+1)*2=?",
            "answer": "Step1. (1+1)\nStep2. (answer*2)"
        },
        {
            "question": "(1+1)*2*2+1=?",
            "answer": "Step1. (1+1)\nStep2. (answer*2)\nStep3. (answer*2)\nStep4. (answer+1)"
        },
        {
            "question": "1+1*2*2+1=?",
            "answer": "Step1. (1*2)\nStep2. (answer*2)\nStep3. (1+answer)\nStep4. (answer+1)"
        },
    ]

    example_prompt = PromptTemplate(
        input_variables=["question", "answer"],
        template="Question: {question}\n{answer}",
    )
    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        suffix="Question: {input}",
        input_variables=["input"],
    )

    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_function_messages(x["intermediate_steps"]),
        }
        | prompt
        | llm
        | OpenAIFunctionsAgentOutputParser()
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Change the input here.
    output = agent_executor.invoke({"input": input})

    operations = re.findall(r'\((.*?)\)', output['output'])

    pre_answer = 0
    for op in operations:
        if 'answer' in op:
            op = op.replace('answer', str(pre_answer))

        if '+' in op:
            pre_answer = int(requests.get('http://agent1:5001/addition', headers={'operation': op}).text)
        elif '*' in op:
            pre_answer = int(requests.get('http://agent1:5001/addition', headers={'operation': op}).text)

    return f"intput: {input} opertaions: {operations} answer: {pre_answer}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)