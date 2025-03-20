# Use Ubuntu as the base image
FROM ubuntu:latest

# Install Python3 and related dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Create a virtual environment
RUN python3 -m venv /home/doc-bd-a1/venv

# Activate the virtual environment and install Python libraries
RUN /home/doc-bd-a1/venv/bin/pip install --upgrade pip
RUN /home/doc-bd-a1/venv/bin/pip install pandas numpy seaborn matplotlib scikit-learn scipy

# Copy the dataset into the container
COPY ./titanic.csv /home/doc-bd-a1/

# Start a bash shell when the container starts
CMD ["/bin/bash"]
