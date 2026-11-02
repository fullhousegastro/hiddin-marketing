FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# [Codex-GR 2026-11-02] Nur der Code, nicht der ganze Kontext (.git, .env); siehe .dockerignore.
COPY *.py ./

CMD ["python", "hiddin_post.py"]
