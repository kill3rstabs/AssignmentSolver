# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the environment variable to tell Django to run the server on all available IPs
ENV PYTHONUNBUFFERED 1

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]