import pandas as pd
import json
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def load_weather_data(file_path):
    with open(file_path, 'r') as file:
        weather_data = json.load(file)['days']
    weather_df = pd.DataFrame(weather_data)
    weather_df['datetime'] = pd.to_datetime(weather_df['datetime'])

    if 'temp' in weather_df.columns:
        weather_df['temp'] = (weather_df['temp'] - 32) * 5 / 9


    weather_df = weather_df[['datetime', 'temp']]
    return weather_df

def load_spotify_data(file_path):
    with open(file_path, 'r') as file:
        spotify_data = json.load(file)
    spotify_df = pd.DataFrame(spotify_data)
    spotify_df['endTime'] = pd.to_datetime(spotify_df['endTime'])
    spotify_df['date'] = spotify_df['endTime'].dt.date
    daily_listening = spotify_df.groupby('date')['msPlayed'].sum().reset_index()
    daily_listening['hours_played'] = daily_listening['msPlayed'] / (1000 * 60 * 60)
    daily_listening['datetime'] = pd.to_datetime(daily_listening['date'])
    return daily_listening[['datetime', 'hours_played']]

def analyze_data(weather_file, spotify_file):
    weather_df = load_weather_data(weather_file)
    spotify_df = load_spotify_data(spotify_file)

    merged_data = pd.merge(weather_df, spotify_df, on='datetime', how='inner')

    correlation, p_value = pearsonr(merged_data['temp'], merged_data['hours_played'])
    print(f"Correlation between temperature and listening time: {correlation:.2f}")
    print(f"P-value: {p_value:.4f}")

    comparison_table = merged_data[['datetime', 'temp', 'hours_played']]
    comparison_table.columns = ['Date', 'Temperature (°C)', 'Listening Time (hours)']

    comparison_table['Date'] = comparison_table['Date'].dt.strftime('%Y-%m-%d')
    comparison_table['Temperature (°C)'] = comparison_table['Temperature (°C)'].map('{:.1f}'.format)
    comparison_table['Listening Time (hours)'] = comparison_table['Listening Time (hours)'].map('{:.2f}'.format)

    print("\nFormatted Comparison Table:\n")
    print(comparison_table)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:orange'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Temperature (°C)', color=color)
    ax1.plot(merged_data['datetime'], merged_data['temp'], label='Temperature (°C)', color=color, linestyle='--', marker='o')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Listening Time (hours)', color=color)
    ax2.plot(merged_data['datetime'], merged_data['hours_played'], label='Listening Time (hours)', color=color, marker='o')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Daily Temperature vs Music Listening Time')
    fig.tight_layout()
    plt.grid(True)
    plt.show()

    return comparison_table

weather_file = 'weather.json'
spotify_file = 'filtered_spotify_data.json'

if __name__ == "__main__":
    analyze_data(weather_file, spotify_file)
