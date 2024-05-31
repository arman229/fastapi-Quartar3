FROM jupyter/jupyter/base-notebook:latest

WORKDIR /code

RUN pip install poetry

COPY . .
RUN poetry config virtualenvs.create.false
EXPOSE 8000
CMD [ "jupyter", "notebook","--port","8000","--no-browser","--allow-root" ]