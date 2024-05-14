# Using the official python docker image as base
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Specify the command to run on container start
CMD [ "python3", "app.py" ]