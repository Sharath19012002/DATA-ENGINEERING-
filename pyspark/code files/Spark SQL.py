# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# COMMAND ----------

df = spark.read.json("/FileStore/tables/bus/people.json")

df.show()


# COMMAND ----------

# Print the schema in a tree format
df.printSchema()

df.select("name").show()

# Select everybody, but increment the age by 1
df.select(df['name'], df['age'] + 1).show()


# Select people older than 21
df.filter(df['age'] > 21).show()

# Count people by age
df.groupBy("age").count().show()

# COMMAND ----------

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")

sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()

# COMMAND ----------

# Register the DataFrame as a global temporary view
df.createGlobalTempView("people")

# Global temporary view is tied to a system preserved database `global_temp`
spark.sql("SELECT * FROM global_temp.people").show()


# Global temporary view is cross-session
spark.newSession().sql("SELECT * FROM global_temp.people").show()
