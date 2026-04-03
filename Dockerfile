# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]