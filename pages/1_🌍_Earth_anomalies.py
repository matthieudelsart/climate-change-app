import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Earth Map Anomalies", page_icon="🌍")

st.title("Visualize Climate Change Data")

# Cache the data loading step
@st.cache_data
def load_data():
    return pd.read_csv('data/world_temperature_anomalies.csv')

st.cache_data()
def filter_data(data, year):
    return data[data['Year'] == year]

# Create a slider for selecting the year (assuming your data has a 'Year' column)
selected_year = st.slider("Select Year", min_value=1975, max_value=2024, value=2023, format="%d")
data = load_data()
filtered_data = filter_data(data, selected_year)

# Create a world map of temperature anomalies for the selected year
fig = px.scatter_geo(filtered_data, lat='Latitude', lon='Longitude', color='Temperature Anomaly',
                     title=f"Global Temperature Anomalies ({selected_year})",
                     color_continuous_scale="RdBu_r",
                     range_color=(-3, 3), opacity=0.3,
                     template="plotly_white")  # Adjust range as necessary

fig.update_geos(
    showcountries=True, countrycolor="black",
    projection_type="natural earth",
    showframe=False,
    coastlinewidth=0.7,
    countrywidth=0.2,
)

fig.update_traces(
    hovertemplate="<b>Latitude:</b> %{lat}<br>"
                  "<b>Longitude:</b> %{lon}<br>"
                  "<b>Anomaly:</b> %{marker.color:+.2f}°C<extra></extra>"
)

# Show the figure in Streamlit
st.plotly_chart(fig)

st.write("This map shows the temperature anomalies across the globe for the selected year. The baseline used is the 1950-1980 average temperature.")