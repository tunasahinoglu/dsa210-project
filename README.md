# Spotify Daily Listening Duration and Weather Analysis
## Motivation
This project aims to uncover and analyze the potential relationship between daily music listening time and weather temperature. Understanding how these two variables interact could provide valuable insights into the ways external environmental factors influence personal habits and behaviors, specifically focusing on music consumption. The connection between weather conditions and human activity is an area that has attracted considerable attention in various disciplines, including psychology and behavioral science, yet relatively little research has been conducted to explore its impact on everyday activities such as listening to music. By delving into this relationship, the project seeks to determine whether certain weather patterns—such as warmer or colder days—lead to noticeable changes in the duration of music listening. The insights gained from this research may help explain broader patterns in how people adjust their daily routines in response to environmental factors, potentially revealing subtle but significant influences of weather on leisure activities.

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

## Sample Data

  ### Spotify Sample Data
    {
            "endTime": "2024-07-25 07:46",
            "artistName": "Chris Isaak",
            "trackName": "Blue Hotel",
            "msPlayed": 3100
        },
        {
            "endTime": "2024-07-25 07:46",
            "artistName": "Mark Knopfler",
            "trackName": "Beryl",
            "msPlayed": 840
        },
        {
            "endTime": "2024-07-25 07:49",
            "artistName": "Mark Knopfler",
            "trackName": "What It Is",
            "msPlayed": 210400
        }

  ### Weather Sample Data
    {
        "datetime" : "2024-07-25",
        "datetimeEpoch" : 1721854800,
        "tempmax" : 87.2,
        "tempmin" : 73.6,
        "temp" : 80.4,
        "feelslikemax" : 88.8,
        "feelslikemin" : 73.6,
        "feelslike" : 81.4,
        "dew" : 67.1,
        "humidity" : 65.3,
        "precip" : 0.0,
        "precipprob" : 0.0,
        "precipcover" : 0.0,
        "preciptype" : null,
        "snow" : 0.0,
        "snowdepth" : 0.0,
        "windgust" : 32.2,
        "windspeed" : 19.6,
        "winddir" : 36.0,
        "pressure" : 1004.8,
        "cloudcover" : 40.0,
        "visibility" : 6.3,
        "solarradiation" : 208.6,
        "solarenergy" : 18.0,
        "uvindex" : 10.0,
        "sunrise" : "05:52:30",
        "sunriseEpoch" : 1721875950,
        "sunset" : "20:25:10",
        "sunsetEpoch" : 1721928310,
        "moonphase" : 0.64,
        "conditions" : "Partially cloudy",
        "description" : "Partly cloudy throughout the day.",
        "icon" : "partly-cloudy-day",
        "stations" : [ "D8508", "LTBA", "17063099999", "17119099999", "17118099999", "17064099999", "17060099999", "17066199999", "LTFJ" ],
        "source" : "obs"
      }
    
---

## Methodology
1. **Data Collection and Cleaning**
   - Spotify data was processed from JSON format to calculate daily, weekly and monthly listening durations.
   - Deleting unnecessary data like brown noise, white noise and so on.
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
Overall, while no strong general correlation was found between daily temperature and music listening duration, more specific patterns emerged when examining particular time frames. This indicates that temperature may influence music listening behavior differently depending on the context and time scale.

1 - Daily Trends:
Analysis of daily variations in listening duration relative to temperature fluctuations revealed moderate shifts, with warmer days showing a tendency towards slightly longer music listening times. While these changes were not extreme, a general pattern emerged where mild increases in temperature appeared to correspond with marginally extended listening periods.

2 - Weekly Patterns:
Aggregating the data on a weekly basis provided more consistent and clearer trends. It was observed that listening time tended to peak during weeks characterized by moderate weather conditions. This suggests that extreme weather, whether hot or cold, may slightly reduce the overall duration of daily music listening, while more temperate conditions encourage higher engagement with music.

3 - Monthly Insights:
A comparative analysis across months highlighted broader seasonal trends.

Warmer months, such as July and August, generally showed slightly decreased overall listening durations compared to colder months like October and November.

In the monthly comparison chart, a noticeable dip in listening time was observed during August and September. Despite the decrease in temperature during this period, listening durations also declined, suggesting that other seasonal factors, such as vacations or outdoor activities, might have influenced this trend.

From September to November, a gradual and steady increase in listening time was evident. This trend coincided with cooler temperatures and the seasonal shift towards more indoor-focused activities, indicating a possible link between colder weather and increased music consumption.

---
# Visualizations

**Daily Spotify Listening Duration**
![spotify](https://github.com/user-attachments/assets/782cd0df-6155-4b14-9c96-bc72c41c97f4)
---
**Daily Temperature Trends**
![weather](https://github.com/user-attachments/assets/5cb3d6c8-4633-4b44-a0c6-bf87801fa1d1)
---
**Daily Comparison of Listening Time and Temperature**
![daily_comparison](https://github.com/user-attachments/assets/9c7bd8a5-18a2-4f1c-b409-3eb3405891b8)
---
**Weekly Comparison of Listening Time and Temperature**
![weekly_comparison](https://github.com/user-attachments/assets/cca99599-8c12-44b5-a11b-8fda85ed7c0e)
---
**Monthly Comparison of Listening Time and Temperature**
![monthly_comparison](https://github.com/user-attachments/assets/13410d6c-043b-4f00-bed9-824595e94e7f)

    
---

## Limitations and Future Work
### Limitations:

  1- The data used in this study is limited to a single year and one specific geographical location, which may restrict the ability to generalize findings to other regions or time periods.
  
  2- Variability in individual listening preferences, external factors such as cultural events, and differences in access to streaming services were not accounted for, which could influence results.

### Future Work:

  1- Collecting data over multiple years and from diverse geographical locations would enhance the robustness of the analysis and improve the generalizability of the findings.
  
  2- Including additional variables, such as precipitation, wind speed, and humidity, could provide a more comprehensive understanding of how weather conditions influence music listening behavior.
  
  3- Conducting surveys or qualitative research alongside quantitative analysis might offer deeper insights into the motivations behind changes in listening patterns during different weather conditions.
  
  4-Exploring the impact of specific genres and moods of music during varying weather conditions could further enrich the study by revealing preferences linked to emotional responses to the environment.





