FROM python:{{cookiecutter.python_version}}-slim-buster
RUN mkdir -p /home/app && addgroup app && useradd -d /home/app -g app app && chown app:app /home/app
RUN apt-get update && apt-get install -y curl
USER app
WORKDIR /home/app
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH=/home/gitlab/.poetry/bin:$PATH
ENV FLAKS_ENV=development
RUN poetry config virtualenvs.in-project true
COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN poetry install --no-dev
COPY . .
