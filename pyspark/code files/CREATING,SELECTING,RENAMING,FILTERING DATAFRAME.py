# Databricks notebook source
import pyspark
from pyspark.sql import SparkSession
# Create a spark session
spark = SparkSession.builder.appName('pyspark - example join').getOrCreate() 
# Create data in dataframe
data = [(('Ram'), '1991-04-01', 'M', 3000),
       (('Mike'), '2000-05-19', 'M', 4000),
       (('Rohini'), '1978-09-05', 'M', 4000),
       (('Maria'), '1967-12-01', 'F', 4000),
       (('Jenis'), '1980-02-17', 'F', 1200)]
# Column names in dataframe
columns = ["Name", "DOB", "Gender", "salary"]
# Create the spark dataframe
df = spark.createDataFrame(data=data,
                          schema=columns)
# Print the dataframe
df.show()

# COMMAND ----------

#Using withColumnRenamed()
#Renaming multiple column names
# Rename the column name 'Gender' to 'Sex'
# Then for the returning dataframe 
# again rename the 'salary' to 'Amount'
df.withColumnRenamed("Gender","Sex").withColumnRenamed("salary","Amount").show()



# COMMAND ----------

#Using selectExpr()

# Select the 'Name' as 'name'
# Select remaining with their original name
data = df.selectExpr("Name as name","DOB","Gender","salary")
 
# Print the dataframe
data.show()



# COMMAND ----------

# Using select() method

# Import col method from pyspark.sql.functions
from pyspark.sql.functions import col
 
# Select the 'salary' as 'Amount' using aliasing
# Select remaining with their original name
data = df.select(col("Name"),col("DOB"),
                 col("Gender"),
                 col("salary").alias('Amount')
# Print the dataframe
data.show()
