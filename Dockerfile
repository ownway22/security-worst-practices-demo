# Intentionally outdated and insecure base image
FROM python:3.8-slim

# Hard-coded secret (for scanners)
ENV SECRET_TOKEN=hardcoded_docker_secret_value

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
