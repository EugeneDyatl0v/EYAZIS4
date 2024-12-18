FROM python:3.12

WORKDIR /app
ENV PYTHONPATH=/app

COPY server/requirements.txt .
RUN set -eux; \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN python -m spacy download en_core_web_sm
RUN python -m spacy download ru_core_news_md

CMD ["uvicorn", "server.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]