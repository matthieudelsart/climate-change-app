import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import Ridge
import numpy as np

ridge = Ridge()

st.set_page_config(page_title="Anomalies in your City", page_icon="🏙️")
st.title("Visualize temperature anomalies in your city")

st.write("Select the cities you want to compare:")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    show_paris = st.checkbox("Paris")
with col2:
    show_new_york = st.checkbox("New York")
with col3:
    show_singapore = st.checkbox("Singapore")
with col4:
    show_tokyo = st.checkbox("Tokyo")
with col5:
    show_london = st.checkbox("London")

st.write("Show projections until 2100:")
show_projections = st.checkbox("**Show projections**")

@st.cache_data
def load_city_data(city):
    path = f'data/{city.lower()}_temperature_anomalies.csv'
    return pd.read_csv(path)

@st.cache_data
def predict_anomalies(city_data, city_name):
    if show_projections:
        data_train = city_data[city_data['Year'] >= 1975]
        ridge.fit(data_train['Year'].values.reshape(-1, 1), data_train['tempanomaly'].values)
        df_pred = pd.DataFrame({'Year': range(1975, 2101)})
        df_pred['tempanomaly'] = ridge.predict(df_pred['Year'].values.reshape(-1, 1))
        return df_pred
    return None

fig = go.Figure()

city_options = {
    "Paris": (show_paris, "blue"),
    "New York": (show_new_york, "red"),
    "Singapore": (show_singapore, "green"),
    "Tokyo": (show_tokyo, "orange"),
    "London": (show_london, "purple"),
}

if show_projections:
    years = np.arange(1880, 2101)
else:
    years = np.arange(1880, 2024)
fig.add_trace(go.Scatter(
    x=years, 
    y=0 * years, 
    mode='lines', 
    line=dict(color='grey', width=1),
    showlegend=False 
))

# Loop through selected cities, add traces if selected
for city_name, (show_city, color) in city_options.items():
    if show_city:
        city_data = load_city_data(city_name.lower().replace(" ", ""))
        # Plot historical data
        fig.add_trace(go.Scatter(
            name=f'{city_name} (hist.)',
            x=city_data['Year'], 
            y=city_data['tempanomaly'], 
            mode='lines',
            line=dict(color=color),
            hoverinfo='x+y+name',
            opacity=0.5,
            hovertemplate='%{x}: %{y:.2f}°C<extra></extra>'
        ))
        
        # Add projections if enabled
        if show_projections:
            pred_data = predict_anomalies(city_data, city_name)
            if pred_data is not None:
                fig.add_trace(go.Scatter(
                    x=pred_data['Year'], 
                    y=pred_data['tempanomaly'], 
                    mode='lines',
                    name=f'{city_name} (proj.)',
                    line=dict(color=color, dash='dash'),
                    hoverinfo='x+y+name',
                    opacity=0.5,
                    hovertemplate='%{x}: %{y:.2f}°C<extra></extra>'
                ))

# Finalize layout 
fig.update_layout(
    title="City Temperature Anomalies per Year vs 1950-1980 average",
    xaxis_title="Year",
    yaxis_title="Temperature Anomaly (°C)",
    yaxis=dict(range=[-2, 6] if show_projections else [-2, 4]),
)

st.plotly_chart(fig)
st.write("This graph shows the yearly historical temperature anomalies as well as the projections until 2100 if the 1975-2023 trend continues.")
