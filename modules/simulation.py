import numpy as np
import pandas as pd


class ProcessSimulator:
    def __init__(self):
        self.base_temperature = 25
        self.base_pressure = 101.3
        self.base_humidity = 45

    def simulate_process(self, hours, variation_factor=1.0):
        """Simulate manufacturing process with given parameters."""
        timestamps = pd.date_range(start='2024-01-01', periods=hours, freq='H')

        # Add random variations
        temperature = np.random.normal(self.base_temperature, 2 * variation_factor, hours)
        pressure = np.random.normal(self.base_pressure, 0.5 * variation_factor, hours)
        humidity = np.random.normal(self.base_humidity, 5 * variation_factor, hours)

        # Simulate defects based on parameter deviations
        defect_prob = self.calculate_defect_probability(temperature, pressure, humidity)
        defects = np.random.binomial(1, defect_prob)

        return pd.DataFrame({
            'timestamp': timestamps,
            'temperature': temperature,
            'pressure': pressure,
            'humidity': humidity,
            'defect': defects
        })

    def calculate_defect_probability(self, temperature, pressure, humidity):
        """Calculate defect probability based on parameter deviations."""
        temp_dev = np.abs(temperature - self.base_temperature) / 2
        pressure_dev = np.abs(pressure - self.base_pressure) / 0.5
        humidity_dev = np.abs(humidity - self.base_humidity) / 5

        return np.clip(0.01 * (temp_dev + pressure_dev + humidity_dev), 0, 1)
