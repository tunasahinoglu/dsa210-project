import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

with open('filtered_spotify_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

records = []
for item in data:
    end_time = datetime.strptime(item['endTime'], "%Y-%m-%d %H:%M")
    duration_minutes = item['msPlayed'] / (1000 * 60)
    records.append({'date': end_time.date(), 'duration_minutes': duration_minutes})

df = pd.DataFrame(records)

daily_stats = df.groupby('date')['duration_minutes'].sum().reset_index()

start_date = datetime(2023, 11, 26).date()
end_date = datetime(2024, 11, 27).date()
filtered_stats = daily_stats[(daily_stats['date'] >= start_date) & (daily_stats['date'] <= end_date)]

plt.figure(figsize=(10, 6))
plt.plot(filtered_stats['date'], filtered_stats['duration_minutes'], marker='o')
plt.title('Daily Spotify Music Listening Duration')
plt.xlabel('Date')
plt.ylabel('Duration (min)')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
