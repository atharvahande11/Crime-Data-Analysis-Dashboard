import os

# --------------------------
# Set environment variables
# --------------------------
# Path to your JDK 17
os.environ["JAVA_HOME"] = r"C:\Users\LENOVO\AppData\Local\Programs\Eclipse Adoptium\jdk-17.0.16.8-hotspot"

# Use Python from your Conda environment
os.environ["PYSPARK_PYTHON"] = r"C:\Users\LENOVO\anaconda3\envs\crimebda\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\LENOVO\anaconda3\envs\crimebda\python.exe"

# --------------------------
# PySpark code
# --------------------------
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("CrimeBDA").getOrCreate()

# Sample data
data = [("Mumbai", 25), ("Delhi", 30), ("Bangalore", 22)]
columns = ["City", "Crime_Count"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show results
df.show()

# Stop Spark session
spark.stop()
