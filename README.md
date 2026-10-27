# NBA Player Statistics Dashboard

An interactive dashboard for exploring and comparing NBA player statistics, built with Python and Streamlit.

## Overview

This project uses NBA statistics to provide an interactive way to explore player performance, compare two players, and visualize scoring leaders.

It was developed as a portfolio project to practice Python, data analysis, and data visualization.

## Features

- **Player search:** Find players and explore their statistics.
- **Player comparison:** Compare two players using selected performance metrics.
- **Radar chart:** Visualize and compare player performance across multiple statistical categories.
- **Top scorers:** Explore a bar chart of the top 10 players by points.
- **Interactive visualizations:** Analyze statistics through charts built with Plotly.

## Technologies

- Python
- Streamlit
- Pandas
- Plotly
- NBA API

## Statistics

The dashboard includes metrics such as:

- Points per game (PTS)
- Rebounds (REB)
- Assists (AST)
- Minutes played (MIN)
- True Shooting Percentage (TS%)

Additional defensive metrics are used in the radar comparison.

## How to Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/GuilhermeNasciimento/nba-dashboard.git
   ```

2. Navigate to the project folder:

   ```bash
   cd nba-dashboard
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

## Data Source

Player statistics are retrieved through the NBA API. Data availability may depend on the API service and network access.

## Purpose

This project demonstrates practical skills in data retrieval, data manipulation, exploratory analysis, and interactive data visualization.

**Note:** This is an educational portfolio project and is not affiliated with the NBA.
