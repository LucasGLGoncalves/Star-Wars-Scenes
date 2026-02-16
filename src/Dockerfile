FROM python:3.11-slim

EXPOSE 80

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ARG SCENE=tranquilo
ARG HEADER_TEXT=tranquilo

ENV SCENE=tranquilo
ENV HEADER_TEXT=tranquilo

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN set -eux; \
  if [ -d "/app/static/gifs" ]; then \
    if [ "${SCENE}" = "batalha" ]; then \
      rm -f /app/static/gifs/tranquilo.gif || true; \
    else \
      rm -f /app/static/gifs/batalha.gif || true; \
    fi; \
  fi

CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:80", "app:app"]
