# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir pydantic

# Run baseline script by default
CMD ["python", "baseline.py"]