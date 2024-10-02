from langchain_openai import ChatOpenAI
import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

output = llm.invoke("What would be the AI equivalent of Hello World?")
print(output)