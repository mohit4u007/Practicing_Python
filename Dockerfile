FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye
# Copy the requirements.txt file into the container
COPY requirements.txt .
# Install additional packages
RUN pip install -r requirements.txt