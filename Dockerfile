# Use an official Python runtime as a parent image
FROM python:3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install pip requirements
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Create a non-root user and give permissions
RUN adduser --disabled-password --gecos "" --uid 5678 appuser \
    && chown -R appuser /app
USER appuser

# Run FastAPI using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
