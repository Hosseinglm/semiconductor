import streamlit as st
import pandas as pd
import numpy as np
import json
from modules.data_processor import DataProcessor

st.set_page_config(page_title="Sample Datasets", layout="wide")


def generate_sample_data():
    data_processor = DataProcessor()
    return data_processor.generate_sample_data()


def save_dataframe(df, format_type):
    if format_type == 'csv':
        return df.to_csv(index=False)
    elif format_type == 'json':
        return df.to_json(orient='records')
    elif format_type == 'parquet':
        return df.to_parquet()


def main():
    st.title("Sample Datasets")

    st.markdown("""
    ### Download Sample Manufacturing Data

    These sample datasets contain simulated semiconductor manufacturing data including:
    - Temperature readings
    - Pressure measurements
    - Humidity levels
    - Defect indicators

    Available formats:
    - CSV (Comma Separated Values)
    - JSON (JavaScript Object Notation)
    - Parquet (Columnar Storage Format)
    """)

    # Generate sample data
    df = generate_sample_data()

    # Create columns for different format downloads
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("CSV Format")
        csv_data = save_dataframe(df, 'csv')
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="semiconductor_data.csv",
            mime="text/csv"
        )

    with col2:
        st.subheader("JSON Format")
        json_data = save_dataframe(df, 'json')
        st.download_button(
            label="Download JSON",
            data=json_data,
            file_name="semiconductor_data.json",
            mime="application/json"
        )

    with col3:
        st.subheader("Parquet Format")
        parquet_data = save_dataframe(df, 'parquet')
        st.download_button(
            label="Download Parquet",
            data=parquet_data,
            file_name="semiconductor_data.parquet",
            mime="application/octet-stream"
        )

    # Preview the data
    st.subheader("Data Preview")
    st.dataframe(df.head())


if __name__ == "__main__":
    main()
