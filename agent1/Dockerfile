FROM python:3.11

WORKDIR /sample_agent

COPY . /sample_agent

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "agent1.py"]