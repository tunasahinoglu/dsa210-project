# Spotify Daily Listening Duration and Weather Analysis
## Motivation
This project aims to uncover the relationship between daily music listening time and weather temperature. Understanding this correlation might provide insights into how external environmental factors influence personal habits like music listening.

---

## Datasets
### 1. **Spotify Data**
- **Source:** Downloaded from Spotify's Privacy page.
- **Details:**
  - Listening date
  - Listening duration (minutes)

### 2. **Weather Data**
- **Source:** Collected from visualcrossing.com as JSON format.
- **Details:**
  - Daily temperature
 
---

## Methodology
1. **Data Collection and Cleaning**
   - Spotify data was processed from JSON format to calculate daily, weekly and monthly listening durations.
   - Weather data was fetched and matched with Spotify data based on the date.
 
2. **Data Integration** 
   - Both datasets were merged on the date field to create a combined dataset with music listening time and corresponding daily temperature.
 
3. **Visualization**
   Multiple visualizations were generated to understand trends and relationships:
    -  Daily comparisons of temperature and listening time.
    -  Weekly and monthly aggregations to highlight broader patterns.

4. **Analysis Scripts**
   Python scripts (weather-spotify-daily.py, weather-spotify-weekly.py, and weather-spotify-monthly.py) were used for all analysis and visualizations.

---

## Findings
    -  Daily temperature and listening duration showed moderate variation across the year.
    -  Warmer months tended to have slightly increased listening durations.

---

## Limitations and Future Work
    -  Data is limited to a single year and one geographical location, which might limit generalizability.
    -  Collect additional years of data for improved statistical reliability.



