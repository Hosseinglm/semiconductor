import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


class DataVisualizer:
    @staticmethod
    def create_time_series(df, column, title):
        """Create interactive time series plot."""
        fig = px.line(df, x='timestamp', y=column, title=title)
        fig.update_layout(
            xaxis_title="Time",
            yaxis_title=column.capitalize(),
            hovermode='x unified'
        )
        return fig

    @staticmethod
    def create_anomaly_scatter(df, x_col, y_col, anomaly_labels, title):
        """Create scatter plot with anomaly highlighting."""
        fig = px.scatter(df, x=x_col, y=y_col, color=anomaly_labels,
                         title=title,
                         color_discrete_map={-1: 'red', 1: 'blue', 0: 'gray'})
        return fig

    @staticmethod
    def create_parameter_distribution(df, column):
        """Create distribution plot for process parameters."""
        fig = px.histogram(df, x=column, title=f'{column.capitalize()} Distribution')
        return fig

    @staticmethod
    def create_correlation_heatmap(df):
        """Create correlation heatmap."""
        corr_matrix = df.corr()
        fig = px.imshow(corr_matrix,
                        title='Parameter Correlation Matrix',
                        aspect='auto')
        return fig