# sample_agent

To build the Docker containers, run `docker-compose build`

To start the Docker containters, run `docker-compose up` then visit `http://localhost:5000/calculator?question=${your question here}=?`

An example is http://localhost:5000/calculator?question=1+1*2*3+1=?

Please store your OpenAI API key in a `.env` file as 

```
OPENAI_API_KEY=${Your Key here}
```