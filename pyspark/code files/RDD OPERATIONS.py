# Databricks notebook source
# reduce operation()
from pyspark import SparkContext
sc = SparkContext.getOrCreate()
reduce_rdd = sc.parallelize([1,3,4,6])
print(reduce_rdd.reduce(lambda x, y : x + y))

# COMMAND ----------

# .count() operation 
from pyspark import SparkContext
sc = SparkContext.getOrCreate()
count_rdd = sc.parallelize([1,2,3,4,5,5,6,7,8,9])
print(count_rdd.count())

# COMMAND ----------

# SaveAsTextFile()
from pyspark import SparkContext
sc = SparkContext.getOrCreate()
save_rdd = sc.parallelize([1,2,3,4,5,6])
save_rdd.saveAsTextFile('file1.txt')

# COMMAND ----------

#take() operation
from pyspark import SparkContext
sc = SparkContext.getOrCreate()
take_rdd = sc.parallelize([1,2,3,4,5,5,6,7,8,9])
print(take_rdd.take(4))

# COMMAND ----------

# first() operation
from pyspark import SparkContext
sc = SparkContext.getOrCreate()
first_rdd = sc.parallelize([1,2,3,4,5,5,6,7,8,9])
print(first_rdd.first())

# COMMAND ----------

# collect() operation
from pyspark import SparkContext
sc = SparkContext.getOrCreate()
collect_rdd = sc.parallelize([1,2,3,4,5,5,6,7,8,9])
print(collect_rdd.collect())
