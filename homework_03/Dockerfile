FROM python:3.11.3-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY blog pyproject.toml poetry.lock ./

RUN pip install --upgrade pip
RUN pip install "poetry==1.4.2"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-ansi --only main




CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000
