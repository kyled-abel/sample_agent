FROM python:3.11

WORKDIR /sample_agent

COPY . /sample_agent

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python", "agent2.py"]