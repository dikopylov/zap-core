# pull official base image
FROM python:3.7.5-buster

RUN mkdir -p web/zapisator/core \
        && chmod 755 web/zapisator/core

WORKDIR /web/zapisator/core

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update \
    && apt-get install -y libpq-dev gcc postgresql-client \
    && pip install --upgrade pip \
    && pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

RUN chmod +x ./entrypoint.sh

CMD ["sh", "./entrypoint.sh"]