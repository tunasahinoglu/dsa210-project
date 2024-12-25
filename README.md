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
1.  Daily Trends:
     -  Moderate variations in listening duration across daily temperature changes.
     -  Some warmer days correlated with slightly longer listening times.
2.  Weekly Patterns:
      - Weekly aggregations revealed consistent trends, with listening time peaking during moderate weather.  
3.  Monthly Insights:
      -  Warmer months generally showed slightly decreased listening durations compared to colder months.
      -  In the monthly comparison chart, a noticeable dip in listening time is observed during August and September, while the temperatures were decreasing, the listening duration also decreased.
      -  A gradual increase in listening time occurs from September to November, corresponding with cooler temperatures and potentially indoor-focused activities.
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
    - Data is limited to a single year and one geographical location, which might limit generalizability.
    - Collect additional years of data for improved statistical reliability.



