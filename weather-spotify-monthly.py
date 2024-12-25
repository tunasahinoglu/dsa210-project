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

    if 'temp' in weather_df.columns and weather_df['temp'].max() > 50:  Fahrenheit if max > 50
        weather_df['temp'] = (weather_df['temp'] - 32) * 5 / 9

    weather_df = weather_df[['datetime', 'temp']]
    weather_df['month'] = weather_df['datetime'].dt.to_period('M')
    weather_df = weather_df.groupby('month')['temp'].mean().reset_index()
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
    daily_listening['month'] = daily_listening['datetime'].dt.to_period('M')
    daily_listening = daily_listening.groupby('month')['hours_played'].mean().reset_index()
    return daily_listening

def analyze_data(weather_file, spotify_file):
    weather_df = load_weather_data(weather_file)
    spotify_df = load_spotify_data(spotify_file)

    merged_data = pd.merge(weather_df, spotify_df, on='month', how='inner')

    correlation, p_value = pearsonr(merged_data['temp'], merged_data['hours_played'])
    print(f"Correlation between temperature and listening time (monthly): {correlation:.2f}")
    print(f"P-value: {p_value:.4f}")

    comparison_table = merged_data[['month', 'temp', 'hours_played']]
    comparison_table.columns = ['Month', 'Average Temperature (°C)', 'Average Listening Time (hours)']
    print("\nMonthly Comparison Table:\n")
    print(comparison_table)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:orange'
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Average Temperature (°C)', color=color)
    ax1.plot(merged_data['month'].astype(str), merged_data['temp'], label='Average Temperature (°C)', color=color, linestyle='--', marker='o')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Average Listening Time (hours)', color=color)
    ax2.plot(merged_data['month'].astype(str), merged_data['hours_played'], label='Average Listening Time (hours)', color=color, marker='o')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Monthly Average Temperature vs Music Listening Time')
    fig.tight_layout()
    plt.grid(True)
    plt.show()

    return comparison_table

weather_file = 'weather.json'
spotify_file = 'filtered_spotify_data.json'

if __name__ == "__main__":
    analyze_data(weather_file, spotify_file)
