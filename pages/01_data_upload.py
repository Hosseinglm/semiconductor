import streamlit as st
import pandas as pd
from modules.data_processor import DataProcessor

st.set_page_config(page_title="Data Upload", layout="wide")


def main():
    st.title("Data Upload and Preprocessing")

    data_processor = DataProcessor()

    # File upload
    uploaded_file = st.file_uploader("Upload manufacturing data (CSV)", type=['csv'])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state['raw_data'] = df

            st.subheader("Raw Data Preview")
            st.dataframe(df.head())

            if st.button("Preprocess Data"):
                with st.spinner("Preprocessing data..."):
                    processed_df = data_processor.preprocess_data(df)
                    st.session_state['processed_data'] = processed_df

                st.success("Data preprocessing completed!")
                st.subheader("Processed Data Preview")
                st.dataframe(processed_df.head())

        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

    # Sample data generation
    if st.button("Generate Sample Data"):
        sample_data = data_processor.generate_sample_data()
        st.session_state['raw_data'] = sample_data
        st.session_state['processed_data'] = data_processor.preprocess_data(sample_data)

        st.success("Sample data generated successfully!")
        st.dataframe(sample_data.head())


if __name__ == "__main__":
    main()
