FROM python:3.11-slim

# Install Nmap
RUN apt-get update && apt-get install -y nmap && rm -rf /var/lib/apt/lists/*

# Install FastAPI + Uvicorn
RUN pip install fastapi uvicorn

WORKDIR /app
COPY app.py /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
