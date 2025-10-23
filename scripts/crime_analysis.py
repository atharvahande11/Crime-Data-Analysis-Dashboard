from pyspark.sql import SparkSession

# Start Spark
spark = SparkSession.builder.appName("CrimeBDA").getOrCreate()

# Load dataset
df = spark.read.csv("data/Chicago_Crimes_2012_to_2017.csv", header=True, inferSchema=True)

# Show first 5 rows
df.show(5)

# Count rows
print("Total records:", df.count())

# Stop Spark
spark.stop()
