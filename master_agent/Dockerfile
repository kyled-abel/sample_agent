FROM python:3.11

WORKDIR /sample_agent

COPY . /sample_agent

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "master_agent.py"]