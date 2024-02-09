# Databricks notebook source
import pyspark
from pyspark.sql import SparkSession

# Create a spark session
spark = SparkSession.builder.appName('pyspark - example join').getOrCreate()

# Create data in dataframe with Indian names
data = [(('Arjun'), '1990-08-15', 'M', 5000),
               (('Priya'), '1985-03-25', 'F', 6000),
               (('Amit'), '1976-11-10', 'M', 7000),
               (('Sonia'), '1988-06-30', 'F', 8000),
               (('Rajesh'), '1982-09-12', 'M', 9000)]

# Column names in dataframe
columns = ["Name", "DOB", "Gender", "salary"]

# Create the spark dataframe
df = spark.createDataFrame(data=data, schema=columns)

# Print the dataframe with Indian names
df.show()


# COMMAND ----------

#Using withColumnRenamed()
#Renaming multiple column name
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
                 col("salary").alias('Amount'))
# Print the dataframe
data.show()
