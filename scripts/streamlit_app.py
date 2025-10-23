import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px

# ---- App Title ----
st.set_page_config(page_title="Crime Data Dashboard - India", layout="wide")
st.title("🕵️ Crime Data Analysis Dashboard - India")
st.markdown("Visualize and analyze crime data interactively with maps and charts.")

# ---- Load Dataset ----
data_path = "data/Chicago_Crimes_2012_to_2017.csv"

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=['Latitude', 'Longitude'])
    return df

with st.spinner("Loading dataset..."):
    df = load_data(data_path)

# ---- Sidebar Filters ----
st.sidebar.header("🔍 Filter Options")

crime_types = df['Primary Type'].unique().tolist()
selected_crime = st.sidebar.selectbox("Select Crime Type", crime_types)

years = sorted(df['Year'].dropna().unique().astype(int))
selected_year = st.sidebar.selectbox("Select Year", years)

filtered_df = df[(df['Primary Type'] == selected_crime) & (df['Year'] == selected_year)]

# ---- Summary Stats ----
st.subheader(f"📊 Crime Summary: {selected_crime} ({selected_year})")
st.write(f"Total Records Found: **{len(filtered_df)}**")

if len(filtered_df) == 0:
    st.warning("No records found for this filter combination.")
    st.stop()

# ---- Limit records for map to avoid lag ----
max_points = 1000
map_df = filtered_df.head(max_points)

if len(filtered_df) > max_points:
    st.info(f"Showing only first {max_points} points on map for performance.")

# ---- Interactive Map ----
st.subheader("🗺️ Crime Map View")

m = folium.Map(
    location=[map_df['Latitude'].mean(), map_df['Longitude'].mean()],
    zoom_start=5,
    tiles="Cartodb Positron"
)

for _, row in map_df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=3,
        color="red",
        fill=True,
        fill_opacity=0.6,
        popup=f"{row['Primary Type']} - {row['Description']}"
    ).add_to(m)

st_folium(m, width=1000, height=550)

# ---- Chart ----
st.subheader("📈 Crimes by Location Description")
chart_df = filtered_df['Location Description'].value_counts().reset_index()
chart_df.columns = ['Location Description', 'Count']

fig = px.bar(
    chart_df.head(15), 
    x='Location Description', 
    y='Count',
    title=f"Top 15 Locations for {selected_crime} ({selected_year})",
    color='Count', 
    color_continuous_scale='Reds'
)
st.plotly_chart(fig, use_container_width=True)

# ---- Footer ----
st.markdown("---")
st.markdown("Developed by **Atharva Hande** | Powered by Streamlit, Folium & Plotly 🎯")
