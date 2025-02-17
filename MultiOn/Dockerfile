# Use the official Python image as the base image
FROM python:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for Playwright
RUN apt-get update

COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt


# Copy the application code into the container
COPY . .