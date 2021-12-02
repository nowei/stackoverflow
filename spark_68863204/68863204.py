import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import SparkContext, SparkConf
from pyspark.sql import Window
from pyspark.sql import functions as f
import pandas as pd
conf = SparkConf()
sc = SparkContext(conf=conf)
spark = SparkSession(sc)
df = spark.read.option('header', True).csv('file.txt',)

w = (Window.partitionBy('category', f.to_date(f.col('timestamp'))).orderBy('timestamp')
      .rangeBetween(Window.unboundedPreceding, 0))

df = df.withColumn('cum_sum_by_category', f.sum('value').over(w))
df.show()