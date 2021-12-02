import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import *
from pyspark.sql.functions import monotonically_increasing_id

conf = SparkConf()
sc = SparkContext(conf=conf)
spark = SparkSession(sc)
data = [[1, {'f':[1,2,3]}], [2, None],[0, None], [1, None], [3, {'f':[1]}]]
schema = StructType([
    StructField('mynum', IntegerType(), True), 
    StructField('mystruct', 
        StructType([StructField('f', ArrayType(IntegerType()), True)]), True)
    ])
rdd = spark.sparkContext.parallelize(data)
df = spark.createDataFrame(rdd, schema)

def get_nulls_nans_zeros(c, df):
    # all inputs
    val = df.select(count(when(isnull(c), c)).alias(c))
    t = type(df.schema[c].dataType)
    # numeric inputs
    if t in [ByteType, ShortType, IntegerType, LongType, FloatType, DoubleType, DecimalType]:
        val = val.union(df.select(count(when(isnan(c), c)).alias(c)))
        val = val.union(df.select(count(when(col(c) == 0, c)).alias(c)))
    return val.select(sum(c).alias(c))

res = [get_nulls_nans_zeros(c, df) for c in df.columns]
res = [r.withColumn("id", monotonically_increasing_id()) for r in res]
result = res[0].join(res[1], "id", "outer").drop("id")
result.show()