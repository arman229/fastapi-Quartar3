FROM python:3.12
LABEL maintainer='Arman ashraf'
WORKDIR /code
RUN pip install poetry
COPY . /code/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root
EXPOSE 8000    
CMD ["poetry", "run", "uvicorn", "devcontainer.main:app", "--host", "0.0.0.0", "--reload"]