# Pull base image
FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/

RUN pipenv install --system --dev

COPY . /code/

EXPOSE 8000
CMD ["python", "main.py"]
