# AI-Driven Semiconductor Manufacturing Optimization Platform

This platform is designed to optimize semiconductor manufacturing processes using AI-driven solutions for real-time monitoring, anomaly detection, and predictive analytics. The platform leverages Python and Streamlit to provide a web-based interface, enabling manufacturers to improve yield rates, reduce defects, and optimize production workflows.

## Key Features

### 1. Real-time Process Monitoring
- Tracks critical manufacturing parameters such as:
  - Temperature
  - Pressure
  - Humidity
- Provides interactive visualizations for trend analysis.
- Shows parameter correlations and distributions.

### 2. Anomaly Detection
- Utilizes multiple machine learning algorithms to detect anomalies:
  - **Isolation Forest** for outlier detection.
  - **DBSCAN** clustering for pattern recognition.
  - **Random Forest** for supervised defect prediction.
- Visualizes anomaly patterns in real time.
- Provides performance metrics for each model.

### 3. Process Simulation
- Simulates semiconductor manufacturing processes with configurable parameters.
- Allows adjustment of variation factors to simulate real-world conditions.
- Calculates defect probabilities based on simulated data.
- Enables what-if scenario analysis for production optimization.

### 4. Data Management
- Supports multiple data formats:
  - CSV
  - JSON
  - Parquet
- Includes sample dataset generation for testing and validation.
- Features data preprocessing and validation steps to ensure data integrity.
- Offers interactive data preview for better insights into the data.

## Technical Stack

- **Python 3.11**: The primary language for backend and machine learning tasks.
- **Streamlit**: Used for building the interactive web interface.
- **Pandas & NumPy**: For data processing and manipulation.
- **Scikit-learn**: For implementing machine learning algorithms.
- **Plotly**: For creating interactive data visualizations and charts.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/semiconductor-manufacturing-optimization.git
   cd semiconductor-manufacturing-optimization

2. python -m venv venv

3. pip install -r requirements.txt

4. streamlit run main.py
