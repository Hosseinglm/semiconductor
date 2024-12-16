import streamlit as st
from modules.ml_models import AnomalyDetector
from modules.visualization import DataVisualizer

st.set_page_config(page_title="Anomaly Detection", layout="wide")


def main():
    st.title("Anomaly Detection")

    if 'processed_data' not in st.session_state:
        st.warning("Please upload or generate data first!")
        return

    df = st.session_state['processed_data']
    detector = AnomalyDetector()
    visualizer = DataVisualizer()

    # Feature selection
    features = ['temperature', 'pressure', 'humidity']
    X = df[features]

    # Anomaly detection
    if st.button("Detect Anomalies"):
        with st.spinner("Detecting anomalies..."):
            anomalies = detector.detect_anomalies(X)

            # Visualize results
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Isolation Forest Results")
                fig1 = visualizer.create_anomaly_scatter(
                    df, 'temperature', 'pressure',
                    anomalies['isolation_forest'],
                    "Isolation Forest Anomaly Detection"
                )
                st.plotly_chart(fig1, use_container_width=True)

            with col2:
                st.subheader("DBSCAN Results")
                fig2 = visualizer.create_anomaly_scatter(
                    df, 'temperature', 'pressure',
                    anomalies['dbscan'],
                    "DBSCAN Clustering Results"
                )
                st.plotly_chart(fig2, use_container_width=True)

    # Train supervised model if defect data is available
    if 'defect' in df.columns:
        if st.button("Train Defect Prediction Model"):
            with st.spinner("Training model..."):
                score = detector.train_supervised(X, df['defect'])
                st.success(f"Model trained successfully! Accuracy: {score:.2f}")


if __name__ == "__main__":
    main()
