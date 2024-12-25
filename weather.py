import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def load_json(file_path: str) -> dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file: {e}")
        return {}

def process_weather_data(data: dict) -> pd.DataFrame:
    records = []
    for day in data.get('days', []):
        date = day.get('datetime')
        temp_f = day.get('temp')
        if date and temp_f is not None:
            records.append({'date': date, 'avg_temp_f': temp_f})
    df = pd.DataFrame(records)
    df['avg_temp_c'] = (df['avg_temp_f'] - 32) * 5 / 9
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    df['month'] = df['date'].dt.strftime('%B')
    return df

def get_unique_months(df: pd.DataFrame) -> pd.DataFrame:
    return df[['date', 'month']].drop_duplicates(subset='month', keep='first')

def plot_temperature(df: pd.DataFrame, unique_months: pd.DataFrame, title: str, xlabel: str, ylabel: str):
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['avg_temp_c'], marker='o', color='orange')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.xticks(unique_months['date'], unique_months['month'], rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    file_path = "weather.json"
    weather_data = load_json(file_path)
    if not weather_data:
        return
    weather_df = process_weather_data(weather_data)
    if weather_df.empty:
        print("No data to process.")
        return
    unique_months_df = get_unique_months(weather_df)
    plot_temperature(
        df=weather_df,
        unique_months=unique_months_df,
        title='Daily Average Temperature (°C)',
        xlabel='Month',
        ylabel='Temperature (°C)'
    )

if __name__ == "__main__":
    main()
