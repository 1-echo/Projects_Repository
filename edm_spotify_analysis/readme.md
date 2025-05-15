# Uncovering Patterns in EDM Music: A Data-Driven Approach (Kaggle)

This project presents a comprehensive exploratory data analysis (EDA) of 700 electronic dance music (EDM) tracks. It focuses on uncovering structural, acoustic, and temporal patterns using Spotify audio features. The analysis combines descriptive statistics, SQL querying, and clustering to understand the characteristics that define EDM and its evolution over time.

## Table of Contents
- [Project Overview](#project-overview)
- [Methodology](#methodology)
- [Tools & Technologies](#tools--technologies)
- [Dataset Description](#dataset-description)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Acknowledgements](#acknowledgements)

## Project Overview

This project provides a deep dive into EDM using a dataset of 700 tracks enriched with Spotify audio features. It reveals how elements like danceability, energy, tempo, and valence vary across artists, keys, years, and subgenres. It also evaluates popularity patterns and applies unsupervised learning to identify track clusters based on their audio profile.

## Methodology

The project follows a structured approach:

1. **Data Overview & Preparation:**
   - Importing and cleaning a CSV dataset formatted for use with Pandas and SQL.
   - Mapping categorical variables (e.g., musical keys) and ensuring data integrity (no missing values).

2. **Exploratory Data Analysis (EDA):**
   - **Univariate Analysis:** Analyzing distributions of danceability, energy, loudness, valence, tempo, etc.
   - **Bivariate & Multivariate Analysis:** Correlations between variables like duration vs. energy, danceability vs. valence.
   - **Categorical Trends:** Year distribution, artist frequency, time signatures, and key preferences.

3. **Clustering & Machine Learning:**
   - Implemented K-Means, Agglomerative Clustering, and BIRCH algorithms to group songs by feature similarity.

4. **SQL Integration:**
   - Custom queries to analyze artist and year frequency, and filter top tracks by popularity.

## Tools & Technologies

- **Python:** Primary programming language.
- **Pandas & NumPy:** Data processing and manipulation.
- **SQLAlchemy & SQLite:** Data querying and integration with Python.
- **Matplotlib & Seaborn:** For rich visualizations including histograms, box plots, scatter plots, and heatmaps.
- **Scikit-learn:** For clustering and data preprocessing.
- **WordCloud:** For artist frequency visualization.
- **Jupyter/Kaggle Notebook:** Interactive environment for end-to-end exploration.

## Dataset Description

The dataset includes structured metadata on 700 EDM tracks, sourced via Spotify’s API. Each entry contains:

- **Track Info:** Track name, artist, album, release year, and duration.
- **Audio Features (18 columns):** Danceability, energy, loudness, key, valence, tempo, speechiness, instrumentalness, acousticness, liveness, and popularity.
- **Time Signature & Mode:** Musical structural elements.

Key statistics:
- No missing data across any field.
- Time range: Tracks span from 1991 to 2024, with peak activity in 2014–2016.
- 93 unique artists, many with multiple entries.

## Exploratory Data Analysis

The analysis revealed several trends:

- **Tempo & Energy:** Most tracks have high energy and tempo clustered between 120–130 BPM.
- **Keys & Time Signatures:** C#, G, F#, and 4/4 time are most common, reflecting genre norms.
- **Valence:** Emotional tone varies, but tracks often center around neutral-to-positive moods.
- **Duration:** Average track length is around 4 minutes, optimized for danceability.
- **Artist Popularity:** Calvin Harris, Avicii, and The Chainsmokers dominate top tracks by popularity.
- **Clustering:** Machine learning methods identified distinct groups of tracks with similar sonic properties.

## Acknowledgements

Special thanks to the Kaggle community and dataset providers for their valuable contributions.

```
  _  __    _    ____  ____ _     _____ 
 | |/ /   / \  / ___|/ ___| |   | ____|
 | ' /   / _ \| |  _| |  _| |   |  _|  
 | . \  / ___ \ |_| | |_| | |___| |___ 
 |_|\_\/_/   \_\____|\____|_____|_____|
 ```

