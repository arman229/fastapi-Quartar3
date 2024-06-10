FROM python:3.12
LABEL maintainer='Arman ashraf'
WORKDIR /code
RUN pip install poetry
COPY . /code/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root
CMD ["poetry", "run", "uvicorn", "kafka_messeging.main:app", "--host", "0.0.0.0" ,"--port", "8000", "--reload"]