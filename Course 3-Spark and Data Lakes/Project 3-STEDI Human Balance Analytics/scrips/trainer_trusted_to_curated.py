import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1690275008605 = glueContext.create_dynamic_frame.from_catalog(
    database="dend",
    table_name="accelerometer_trusted",
    transformation_ctx="AccelerometerTrusted_node1690275008605",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1690274998131 = glueContext.create_dynamic_frame.from_catalog(
    database="dend",
    table_name="step_trainer_trusted",
    transformation_ctx="StepTrainerTrusted_node1690274998131",
)

# Script generated for node Join
Join_node1690275037055 = Join.apply(
    frame1=StepTrainerTrusted_node1690274998131,
    frame2=AccelerometerTrusted_node1690275008605,
    keys1=["sensorreadingtime"],
    keys2=["timestamp"],
    transformation_ctx="Join_node1690275037055",
)

# Script generated for node Drop Fields
DropFields_node1690275056039 = DropFields.apply(
    frame=Join_node1690275037055,
    paths=["user"],
    transformation_ctx="DropFields_node1690275056039",
)

# Script generated for node Machine Learning Curated
MachineLearningCurated_node1690275064394 = glueContext.write_dynamic_frame.from_catalog(
    frame=DropFields_node1690275056039,
    database="dend",
    table_name="machine_learning_curated",
    transformation_ctx="MachineLearningCurated_node1690275064394",
)

job.commit()
