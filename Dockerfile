# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy model.py
COPY model.py .

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python", "model.py"]