# Vizualizing Climate Change

## Description

This project was developped for a class project on using Streamlit with Docker. It leverages plotly to vizualize climate change on two aspects:
- Global temperature anomalies vs 1950-1980 averages at a latitude x longitude granularity
- Evolution of temperatures in 5 cities, as well as the projections until 2100 is we follow the ongoing trends

The app hosted on Streamlit Community Hub can be found [here](https://mdelsart-climate-change-app.streamlit.app/).

It was built based on the [GISTEMP](https://data.giss.nasa.gov/gistemp/) data on historical temperature anomalies.

Global map:
![Earth image](images/earth.png)

City temperatures:
![Cities](images/cities.png)

## Installation

### Prerequisites
- Python 3.7 or higher
**or**:
- Docker

## Usage

### Option 1: Run Streamlit app locally

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

### Option 2: Run with Docker
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
