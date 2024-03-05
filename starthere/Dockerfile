# Use a lightweight Linux distribution as base image
FROM python:3-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies required by the Python application
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
