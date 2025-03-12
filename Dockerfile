# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
