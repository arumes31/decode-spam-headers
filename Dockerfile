# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 18545

# Define environment variable
ENV FLASK_APP=web_gui.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=18545

# Run the app
CMD ["flask", "run"]
