import streamlit as st
from modules.simulation import ProcessSimulator
from modules.visualization import DataVisualizer

st.set_page_config(page_title="Process Simulation", layout="wide")


def main():
    st.title("Process Simulation")

    simulator = ProcessSimulator()
    visualizer = DataVisualizer()

    # Simulation parameters
    col1, col2 = st.columns(2)

    with col1:
        hours = st.slider("Simulation Duration (hours)", 24, 168, 48)
        variation_factor = st.slider("Process Variation Factor", 0.1, 2.0, 1.0)

    # Run simulation
    if st.button("Run Simulation"):
        with st.spinner("Running simulation..."):
            simulated_data = simulator.simulate_process(hours, variation_factor)
            st.session_state['simulated_data'] = simulated_data

            # Visualize results
            st.subheader("Simulation Results")

            # Parameter trends
            for parameter in ['temperature', 'pressure', 'humidity']:
                fig = visualizer.create_time_series(
                    simulated_data, parameter,
                    f"Simulated {parameter.capitalize()} Trend"
                )
                st.plotly_chart(fig, use_container_width=True)

            # Defect analysis
            st.subheader("Simulated Defect Analysis")
            defect_rate = simulated_data['defect'].mean() * 100
            st.metric("Defect Rate", f"{defect_rate:.2f}%")


if __name__ == "__main__":
    main()
