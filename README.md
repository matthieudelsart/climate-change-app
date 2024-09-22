# Vizualizing Climate Change (Streamlit-and-Docker-basics)

## Description
This project demonstrates the basics of using Streamlit with Docker. To do so, we are using two visualizations based on the [GISTEMP](https://data.giss.nasa.gov/gistemp/) data on historical temperatuer anomalies.

![Earth image](images/image.png)

The app hosted on Streamlit Community Hub can be found [here](https://mdelsart-climate-change-app.streamlit.app/).

## Installation

### Prerequisites
- Python 3.7 or higher
or:
- Docker

## Usage

### Option 1: Running Streamlit App Locally

1. Clone the repository:
    ```sh
    git clone https://github.com/matthieudelsart/climate-change-app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd climate-change-app
    ```

3. Run the Streamlit root page:
    ```sh
    streamlit run Welcome.py
    ```

### Running with Docker
1. Build the Docker image:
    ```sh
    docker pull mdelsart/climate-change-app
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8501:8501 mdelsart/climate-change-app
    ```

3. Open your browser and go to `http://localhost:8501` to see the app.

If need be, the docker image can be found there `https://hub.docker.com/repository/docker/mdelsart/climate-change-app`
