🚀Setup Guide

Follow these steps to get the CrimeBDA project running on your local machine.

1️⃣ Clone the Repository
git clone https://github.com/<your-username>/CrimeBDA.git
cd CrimeBDA

2️⃣ Create a Python Virtual Environment

We recommend using conda for easy package management:

conda create -n crimebda python=3.10
conda activate crimebda

3️⃣ Install Required Packages

All dependencies are listed in requirements.txt. Install them using:

pip install -r requirements.txt


Key packages used:

PySpark – for Big Data processing

Pandas – for data manipulation

Streamlit – for interactive web UI

Folium & streamlit-folium – for interactive maps

Plotly – for charts and visualizations

4️⃣ Add the Dataset

Download the Chicago Crimes Dataset (2012–2017) in CSV format and place it in the data/ folder.
Dataset Kaggle link : https://www.kaggle.com/datasets/currie32/crimes-in-chicago?resource=download
Example path:

CrimeBDA/data/Chicago_Crimes_2012_to_2017.csv

5️⃣ Run the Streamlit App

Launch the interactive dashboard:

streamlit run scripts/streamlit_app.py


Open the URL shown in your terminal (usually http://localhost:8501) in your browser.

6️⃣ Explore the Dashboard

Use the sidebar filters to select crime type and year.

View crime hotspots on the map with pins and heatmaps.

Analyze crime locations using interactive charts.

7️⃣ Optional: Run PySpark Scripts

For data preprocessing or analysis with PySpark:

python scripts/crime_analysis.py


✅ Now you’re all set! You can explore, visualize, and analyze Chicago crime data interactively.
