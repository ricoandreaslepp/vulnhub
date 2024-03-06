# Use a lightweight Linux distribution as base image
FROM python:3-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port that the application runs on
EXPOSE 31337

# Command to run the application
CMD ["python", "app.py"]
