import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Config
num_machines = 5
duration_days = 1
sampling_rate_minutes = 5

# Time range
timestamps = pd.date_range(
    start=datetime.now() - timedelta(days=duration_days),
    end=datetime.now(),
    freq=f'{sampling_rate_minutes}min'
)

data = []
for machine_id in range(1, num_machines + 1):
    for ts in timestamps:
        temp = np.random.normal(70, 5)
        vib = np.random.normal(1.5, 0.3)
        status = np.random.choice(['Running', 'Idle', 'Fault'], p=[0.7, 0.2, 0.1])
        data.append([ts, machine_id, temp, vib, status])

df = pd.DataFrame(data, columns=['timestamp', 'machine_id', 'temperature', 'vibration', 'status'])
df.to_csv('data/sensor_data.csv', index=False)
