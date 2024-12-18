FROM python:3.12

WORKDIR /app
ENV PYTHONPATH=/app

COPY server/requirements.txt .
RUN set -eux; \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "-m", "alembic", "-c", "database/alembic/alembic.ini", "upgrade", "head"]