import streamlit as st

st.set_page_config(
    page_title="Semiconductor Manufacturing Optimization",
    page_icon="🏭",
    layout="wide"
)


def main():
    st.title("Semiconductor Manufacturing Optimization Platform")

    st.markdown("""
    ### Welcome to the AI-Driven Manufacturing Optimization Platform

    This platform helps optimize semiconductor manufacturing processes through:
    - Real-time process monitoring
    - Anomaly detection
    - Predictive analytics
    - Process simulation

    ### Getting Started
    1. Download sample datasets in CSV, JSON, or Parquet format
    2. Upload your manufacturing data or use the downloaded sample data
    3. Monitor real-time process parameters
    4. Detect anomalies using advanced ML models
    5. Simulate process variations and analyze outcomes

    Use the sidebar to navigate between different features.
    """)

    # Display system status
    st.sidebar.title("System Status")
    if 'processed_data' in st.session_state:
        st.sidebar.success("✅ Data loaded")
    else:
        st.sidebar.warning("⚠️ No data loaded")


if __name__ == "__main__":
    main()
