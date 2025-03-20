

Titanic Dataset Analysis with Docker

=========================================================

Overview

This project involves performing data preprocessing, exploratory data analysis (EDA), and K-means clustering on the Titanic dataset using Docker. The pipeline processes the dataset step by step, running multiple Python scripts. Finally, the processed data and results are transferred from the Docker container to the local machine.

=========================================================

Requirements

- Docker: To build and run the container.
- Python: Python 3.x is used for the scripts inside the container.
- Libraries: The project uses `pandas`, `numpy`, `seaborn`, `matplotlib`, `scikit-learn`, and `scipy`.

=========================================================


 Step-by-Step Guide

Step 1: Build the Docker Image

    First, the Docker image must be built from the Dockerfile. This image will contain all the necessary dependencies to run the project and execute Python scripts.

Step 2: Run the Docker Container

    Once the Docker image is built, the container can be started. If the container name is already in use, it can either be renamed or removed before starting a fresh container.

Step 3: Running the Python Scripts Inside the Container

    Once inside the container, the following Python scripts should be executed in sequence to process the Titanic dataset:


1. Load Data (`load.py`)

    This script loads the dataset into a pandas DataFrame.

2. Data Preprocessing (`dpre.py`)

    This script performs data cleaning, transformation, and reduction on the dataset. It generates a preprocessed dataset file.

3. Exploratory Data Analysis (`eda.py`)

    This script performs exploratory data analysis (EDA) and generates insights based on the data. The insights are saved as text files.

4. K-means Clustering (`model.py`)

    This script performs K-means clustering on the dataset and generates a clustered dataset.

5. Visualization (`vis.py`)

    This script generates a visualization of the dataset and saves it as a PNG file.

=========================================================


Step 4: Transfer Output Files From the Container to Your Local Machine

After running all the Python scripts, several output files will be generated inside the container. These files need to be copied from the container to your local machine.

=========================================================

The output files include:

- `eda-in-1.txt`, `eda-in-2.txt`, `eda-in-3.txt`: Insights from the exploratory data analysis.
- `res_dpre.csv`: The preprocessed dataset.
- `res_kmeans.csv`: The dataset with K-means clustering labels.
- `vis.png`: A visualization of the dataset.
- `k.txt`: The number of records in each K-means cluster.

=========================================================



Step 5: Use a Bash Script for Automation

You can automate the process of copying all files from the container to your local machine using a simple bash script. The script will ensure that all output files are saved to the appropriate directory on your local system.

After copying the files, the container will be stopped automatically.

=========================================================


Final Outputs

Once the bash script is executed, the following output files will be saved to your local machine in the `service-result/` directory:

- `eda-in-1.txt`, `eda-in-2.txt`, `eda-in-3.txt`: Insights from the exploratory data analysis.
- `res_dpre.csv`: The preprocessed dataset.
- `res_kmeans.csv`: The dataset with K-means clustering labels.
- `vis.png`: A visualization of the dataset.
- `k.txt`: The number of records in each K-means cluster.

=========================================================


Conclusion

This project demonstrates the use of Docker to containerize a data science pipeline. The Titanic dataset is loaded, preprocessed, analyzed, clustered, and visualized using a series of Python scripts running inside a Docker container. The output files are then transferred to the local machine for further analysis or reporting.

=========================================================

Commends that i used it


I see! You are asking for a summary of all the specific commands you ran within Docker and their usage. Here's the list of the commands you've used and their corresponding explanations:

---

1. `python3 load.py /home/doc-bd-a1/titanic.csv`
   - Usage: Runs the `load.py` Python script and loads the Titanic dataset.
   - Explanation: This command loads the data from the `titanic.csv` file into the pandas DataFrame and saves it to `titanic_loaded.csv`.

---

2. `python3 dpre.py /home/doc-bd-a1/titanic.csv`
   - Usage: Runs the `dpre.py` Python script to perform data preprocessing.
   - Explanation: This command reads the Titanic dataset and performs operations like filling missing values, dropping unnecessary columns, and scaling the data. It then saves the preprocessed data to `res_dpre.csv`.

---

3. `python3 eda.py /home/doc-bd-a1/res_dpre.csv`
   - Usage: Runs the `eda.py` Python script for Exploratory Data Analysis.
   - Explanation: This command reads the preprocessed data (`res_dpre.csv`), performs EDA tasks (like finding insights), and saves those insights as text files (`eda-in-1.txt`, `eda-in-2.txt`, `eda-in-3.txt`).

---

4. `python3 model.py /home/doc-bd-a1/res_dpre.csv`
   - Usage: Runs the `model.py` Python script for clustering.
   - Explanation: This command reads the preprocessed data (`res_dpre.csv`), applies K-means clustering with `k=3`, and saves the results into `res_kmeans.csv`. It also generates a `k.txt` file containing the count of records in each cluster.

---

5. `python3 vis.py`
   - Usage: Runs the `vis.py` Python script to generate a visualization.
   - Explanation: This command creates a bar plot of the 'Survived' column from the Titanic dataset, saves the visualization as `vis.png`, and displays the survival counts.

---

6. `docker run -it --name bigdata-container bigdata-img`
   - Usage: Starts a new container from the `bigdata-img` image.
   - Explanation: This command runs a Docker container with the name `bigdata-container` from the built image `bigdata-img` in an interactive terminal session.

---

7. `docker exec -it bigdata-container /bin/bash`
   - Usage: Opens an interactive shell (Bash) in the running container.
   - Explanation: This allows you to execute commands directly inside the container, such as running Python scripts or inspecting files.

---

8. `docker cp C:/Users/amr elabiad/Documents/bd-a1/titanic.csv bigdata-container:/home/doc-bd-a1/`
   - Usage: Copies the `titanic.csv` file from the local machine to the container.
   - Explanation: This copies the dataset to the `/home/doc-bd-a1/` directory inside the container, making it available for use by Python scripts.

---

9. `docker cp bigdata-container:/home/doc-bd-a1/eda-in-1.txt C:/Users/amr elabiad/Documents/bd-a1/service-result/`
   - Usage: Copies the output file `eda-in-1.txt` from the container to the local machine.
   - Explanation: This allows you to retrieve the results from the container and store them in the `service-result/` directory on your local machine.

---

10. `docker ps`
   - Usage: Lists all running containers.
   - Explanation: This helps you monitor which containers are currently running on your system.

---

11. `docker ps -a`
   - Usage: Lists all containers (including those that are stopped).
   - Explanation: This provides information about both running and stopped containers on your system.

---

12. `docker stop bigdata-container`
   - Usage: Stops the running container `bigdata-container`.
   - Explanation: Stops the container after you've finished running your tasks within it.

---

13. `docker rm bigdata-container`
   - Usage: Removes the stopped container `bigdata-container`.
   - Explanation: This deletes the container after it has been stopped, freeing up resources.

---

14. **`docker rename bigdata-container old-bigdata-container`
   - Usage: Renames the container `bigdata-container` to `old-bigdata-container`.
   - Explanation: This allows you to rename an existing container, which is useful if you need to reuse the same container name for another container.

---

15. `docker exec -it bigdata-container ls /home/doc-bd-a1/`
   - Usage: Lists the contents of the `/home/doc-bd-a1/` directory in the running container.
   - Explanation: This helps you verify that the necessary files (like `titanic.csv`) are in the correct directory inside the container.

---

16. `docker rmi bigdata-img`
   - Usage: Removes the Docker image `bigdata-img`.
   - Explanation: This command deletes the image from your local system. Use this when you no longer need the image.

---

These are all the commands that you've used to build the Docker container, run the necessary Python scripts inside it, and manage the container itself. Each of these commands plays a critical role in the data processing pipeline and the container management process.



=========================================================



This README provides a step-by-step guide to setting up, running, and using this project. Ensure that the file paths and other configurations are adjusted based on your environment and setup.