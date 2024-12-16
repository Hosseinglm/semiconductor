import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


class DataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy='mean')

    def preprocess_data(self, df):
        """Preprocess the manufacturing data."""
        # Handle missing values
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        df[numeric_columns] = self.imputer.fit_transform(df[numeric_columns])

        # Scale numeric features
        df[numeric_columns] = self.scaler.fit_transform(df[numeric_columns])

        return df

    def validate_data(self, df):
        """Validate the input data format."""
        required_columns = ['timestamp', 'temperature', 'pressure', 'humidity']
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

        return True

    def generate_sample_data(self):
        """Generate sample manufacturing data for testing."""
        np.random.seed(42)
        n_samples = 1000

        data = {
            'timestamp': pd.date_range(start='2024-01-01', periods=n_samples, freq='H'),
            'temperature': np.random.normal(25, 2, n_samples),
            'pressure': np.random.normal(101.3, 0.5, n_samples),
            'humidity': np.random.normal(45, 5, n_samples),
            'defect': np.random.choice([0, 1], size=n_samples, p=[0.95, 0.05]).astype(int)
        }

        return pd.DataFrame(data)
