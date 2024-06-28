# Football Data Scraper

This repository contains a Python notebook designed for scraping football data from various sources. The main goal of this project is to collect detailed player statistics from the past season to create a comprehensive football database for further analysis.

## Introduction

This is my first attempt at building a football database. As a data science student in college, I am passionate about football and data analysis, and this project is a step towards combining these interests. By collecting and analyzing data from past football seasons, I aim to uncover insights and trends that can be useful for various applications in the football industry.

## Project Overview

The project consists of a Jupyter notebook that scrapes and processes football data into a structured format. The data includes a wide range of player statistics across different aspects of the game, such as defense, goalkeeping, passing, and more.

## Key Features

### Player Statistics
Detailed statistics for players, including their performance in various areas like defense, goalkeeping, passing, shooting, and more.

### Data Organization
The data is organized into multiple tables, each focusing on a specific aspect of the game, such as defense, goalkeeping, passing types, and playing time.

### Comprehensive Analysis
The collected data can be used for in-depth analysis and research, providing insights into player performance and team dynamics.

## Leagues Contained

The data covers various leagues split by country. The leagues included are only those that contain all the detailed data that FBref provides. Leagues that do not have advanced stats such as passing and pass types are not included.

#### European Leagues
- **England** : Premier League - Championship (EFL)
- **Spain** : La Liga - Segunda Division
- **Italy** : Serie A - Serie B
- **Germany** : Bundesliga - 2. Bundesliga
- **France** : Ligue 1 - Ligue 2
- **Portugal** : Primeira Liga
- **Netherlands** : Eredivisie
- **Belgium** : Pro League

#### American Leagues
- **USA** : MLS (east & west)
- **Argentina** : Primera Division
- **Brazil** : Serie A (Brazilian League)
- **Mexico** : Liga MX

*Note that Brazil's 1st division is called "Serie A" too but was changed to "Brazilian League" to avoid confusion*

## Installation

To run this project, ensure you have Python installed. You can clone the repository and install the required libraries using the following commands:

```
git clone <repository_url>
cd <repository_directory>
pip install -r requirements.txt
```

## Usage
Open the Jupyter notebook data-scraping.ipynb in your Jupyter environment and follow the instructions provided in the notebook to scrape and process the football data.

## Motivation and Goals
As a football enthusiast and data science student, my goal is to break into the field of football data analysis. This project is an opportunity to apply my data science skills to real-world football data, gaining practical experience and insights that will be valuable for my future career. By analyzing past seasons' data, I hope to identify patterns and trends that can contribute to a deeper understanding of the game.

## Contributing
Feel free to submit issues or pull requests if you would like to contribute to this project. Make sure to follow the repository's contribution guidelines.

## Data Source
The data for this project is sourced from <a href='https://fbref.com/en/comps/'>FBref</a>. Only leagues with comprehensive detailed data provided by FBref are included in this dataset. Leagues without advanced statistics such as passing and pass types are excluded.

## Kaggle Database
The processed database will be available on Kaggle for further analysis. You can find the dataset <a href='https://www.kaggle.com/datasets/anisguechtouli/football-leagues-data-2023-2024'>here</a>.</br>
*The dataset provided here was further cleaned personally by me after scraping, so the results of the scraping notebook won't be identical to the data in the database.*
