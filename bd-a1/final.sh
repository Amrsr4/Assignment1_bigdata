#!/bin/bash

# Define the destination directory on your local machine
LOCAL_DIR="C:/Users/amr elabiad/Documents/bd-a1/service-result"

# Create the directory if it doesn't exist
mkdir -p "$LOCAL_DIR"

# Copy the output files from the container to your local machine
docker cp bigdata-container:/home/doc-bd-a1/res_dpre.csv "$LOCAL_DIR/"
docker cp bigdata-container:/home/doc-bd-a1/eda-in-1.txt "$LOCAL_DIR/"
docker cp bigdata-container:/home/doc-bd-a1/eda-in-2.txt "$LOCAL_DIR/"
docker cp bigdata-container:/home/doc-bd-a1/eda-in-3.txt "$LOCAL_DIR/"
docker cp bigdata-container:/home/doc-bd-a1/k.txt "$LOCAL_DIR/"
docker cp bigdata-container:/home/doc-bd-a1/vis.png "$LOCAL_DIR/"
docker cp bigdata-container:/home/doc-bd-a1/res_kmeans.csv "$LOCAL_DIR/"
docker cp bigdata-container:/home/doc-bd-a1/titanic_loaded.csv "$LOCAL_DIR/"

# Stop the container after the files are copied
docker stop bigdata-container

# Optional: Print a message indicating that the process is complete
echo "Files copied and container stopped successfully!"
