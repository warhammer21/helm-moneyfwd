# Stage 1: Build stage with Poetry
FROM python:3.9-slim AS builder

WORKDIR /tmp

# Install Poetry
RUN pip install poetry

# Copy Poetry files
COPY pyproject.toml poetry.lock* /tmp/

# Install dependencies and export to requirements.txt
RUN poetry export --without-hashes -f requirements.txt -o requirements.txt

# Stage 2: Runtime stage
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the exported requirements file
COPY --from=builder /tmp/requirements.txt /app/requirements.txt

# Install the required packages
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=run.py

# Expose the port that the app runs on
EXPOSE 8000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
