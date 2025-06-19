# Industrial Sensor Dashboard MVP

This project is a dashboard designed to demonstrate how sensor data from an industrial environment (such as temperature, pressure, and vibration) can be cleaned, processed, and visualized for real-time insights. It simulates what might be deployed in a smart factory or a digital manufacturing testbed such as MITC.

## 🚀 Project Overview

The goal is to:

- Clean and process raw sensor data
- Aggregate and engineer useful metrics
- Create a dashboard to visualize time trends and threshold alerts
- Deliver insights that can assist operators and engineers in decision-making

## 📊 Dashboard Features

The Power BI dashboard (or alternative) includes:

- Line graphs showing temperature/pressure over time
- Highlighted alert zones when thresholds are breached
- Average, min, and max sensor readings
- Sensor status indicators (e.g., overheating or anomalous patterns)
- Filter by sensor ID, date range, or data type

## 📁 Data

- **Input Format:** CSV (simulated IoT sensor output)
- **Fields:** `timestamp`, `sensor_id`, `temperature`, `pressure`, `vibration`

> Sample dataset provided in `data/sensor_data.csv`

## 🧹 Data Processing

Performed using Python:

- Converted timestamps to datetime
- Filtered out null or corrupted entries
- Applied smoothing and rolling average
- Engineered alert flags and summary metrics

Notebook: `notebooks/data_cleaning.ipynb`

## 🛠️ Tools Used

- Python (Pandas, NumPy, Matplotlib)
- Power BI Desktop (or Metabase/Superset as fallback)
- CSV for mock data input

## 💡 Future Improvements

- Real-time ingestion using MQTT or REST
- Deployment on cloud dashboards (e.g., Azure Power BI)
- Integration with ERP/MES APIs
- Predictive maintenance model integration (e.g., anomaly detection)

## 📷 Screenshots

> Add 2–3 screenshots

---

## 🔗 Related

- [MITC](https://mitc.nu)
- [Power BI](https://powerbi.microsoft.com/)
- [Metabase](https://www.metabase.com/)
