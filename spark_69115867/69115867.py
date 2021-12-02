import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import SparkContext, SparkConf
from pyspark.sql import functions as F
conf = SparkConf()
sc = SparkContext(conf=conf)
spark = SparkSession(sc)
df = sc.parallelize([({"A":1, "B":2},), ({"A":3,"B":4},), ({"A":5,"B":6},)]).toDF(['Body'])
keys = ['A', 'B']
key_cols = list(map(lambda f: F.col("Body").getItem(f).alias(str(f)), keys))
final_cols = df.select(key_cols)
final_cols.show()

# df.select(col('body.*'))