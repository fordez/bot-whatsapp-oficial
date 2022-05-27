FROM  python:3.9-slim

COPY ./src /src
COPY ./requeriments.txt /src

RUN pip install --upgrade pip
RUN pip3 install -r ./src/requeriments.txt

CMD ["uvicorn", "src.bot:bot", "--host=0.0.0.0", "--port=8080", "--reload"]
