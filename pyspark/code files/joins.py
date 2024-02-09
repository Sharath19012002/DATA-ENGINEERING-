# Databricks notebook source
import pyspark
from pyspark.sql import SparkSession
# Create SparkSession 
spark = SparkSession.builder.appName('Practice').getOrCreate()
dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
rdd=spark.sparkContext.parallelize(dataList)
result = rdd.collect()
("RDD Contents:", result)

# COMMAND ----------

emp = [(1,"Smith",-1,"2018","10","M",3000),(2, "Rose",1 , "2010", "20","M", 4000),(3,"Williams",1,"2010","10","M",1000),(4, "Jones",2 ,"2005","10","F",2000),(5,"Brown",2,"2010","40","",-1),(6, "Brown", 2, "2010","50","",-1)]
empColumns = ["emp_id","name","superior_emp_id","year_joined", "emp_dept_id","gender","salary"]
empDF = spark.createDataFrame(data=emp, schema = empColumns)
empDF.printSchema()
empDF.show()
dept = [("Finance",10),("Marketing",20),("Sales",30),("IT",40)]
deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.printSchema()
deptDF.show()

# COMMAND ----------

empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"inner") .show()

# COMMAND ----------

empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"outer").show()

# COMMAND ----------

empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"full").show()


# COMMAND ----------

empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"fullouter").show()


# COMMAND ----------

#left join
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"left").show()


# COMMAND ----------

#left join 
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"right").show()


# COMMAND ----------

empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"leftouter").show()


# COMMAND ----------

empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"right").show()

# COMMAND ----------

empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"rightouter").show()


# COMMAND ----------

#left semi join
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"leftsemi").show()


# COMMAND ----------

#left anti join
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"leftanti").show()
