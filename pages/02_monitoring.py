import streamlit as st
from modules.visualization import DataVisualizer
import plotly.express as px

st.set_page_config(page_title="Real-time Monitoring", layout="wide")


def main():
    st.title("Real-time Process Monitoring")

    if 'processed_data' not in st.session_state:
        st.warning("Please upload or generate data first!")
        return

    df = st.session_state['processed_data']
    visualizer = DataVisualizer()

    # Parameter selection
    parameter = st.selectbox("Select Parameter to Monitor",
                             ['temperature', 'pressure', 'humidity'])

    # Time series visualization
    st.subheader(f"{parameter.capitalize()} Over Time")
    fig = visualizer.create_time_series(df, parameter, f"{parameter.capitalize()} Trends")
    st.plotly_chart(fig, use_container_width=True)

    # Distribution analysis
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Parameter Distribution")
        dist_fig = visualizer.create_parameter_distribution(df, parameter)
        st.plotly_chart(dist_fig, use_container_width=True)

    with col2:
        st.subheader("Correlation Matrix")
        corr_fig = visualizer.create_correlation_heatmap(
            df[['temperature', 'pressure', 'humidity']])
        st.plotly_chart(corr_fig, use_container_width=True)


if __name__ == "__main__":
    main()
